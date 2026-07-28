from google.adk.agents import LoopAgent, LlmAgent, BaseAgent
from google.adk.events import Event, EventActions
from google.adk.agents.invocation_context import InvocationContext
from typing import AsyncGenerator

random_generator = LlmAgent(
    name='RandomGenerator',
    model='gemini-3.1-flash-lite-preview',
    description='랜덤한 메세지를 생성하는 에이전트입니다. 스팸 메세지와 정상적인 메세지를 60:40 비율로 생성합니다.',
    output_key='random_messages',
    instruction='스팸 메세지와 정상적인 메세지를 60:40 확률로 생성합니다. 스팸 메ㅐ세지는 "[웹발신]"을 앞에 넣고, 정상적인 메세지는 따로 표시하지 않아도 됩니다. 반드시 하나의 메세지만 출력해야 합니다.'
)

spam_checker = LlmAgent(
    name='SpamChecker',
    model='gemini-3.1-flash-lite-preview',
    instruction='{random_message}이 스팸인지 확인하세요. 스팸이면 "Fail", 아니면 "Pass"를 반환하세요.',
    output_key='spam_status'
)

# 상태를 확인하고, 정상적인 메세지면 루프를 중단하도록 요청하는 커스텀 에이전트
class CheckStatusAndEscalate(BaseAgent):
    async def _run_async_impl(
            self, ctx: InvocationContext # InvocationContext: 이번 실행에 대한 모든 정보를 저장한 객체
    ) -> AsyncGenerator[Event, None]: # Event: 이 함수가 yield로 내보내는 것, None: 밖에서 이 Generator로 보낼 수 있는 값
        status = ctx.session.state.get("spam_status",'Fail') # get의 두 번쨰 인자(여기선 Fail)은 디폴트값
        should_stop = status == "Pass" # Pass 상태면 루프 중지
        yield Event(author=self.name, actions=EventActions(escalate=should_stop))

root_agent = LoopAgent(
    name="SpamCheckLoop",
    max_iterations=10,
    sub_agents=[
        random_generator,
        spam_checker,
        CheckStatusAndEscalate(name='StopChecker')
    ]
)