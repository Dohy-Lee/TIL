import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter  
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory 

# 환경 변수 로드
load_dotenv("./.env")
api_key = os.getenv("OPENAI_API_KEY")

# PDF 처리 함수
@st.cache_resource
def process_pdf():
    loader = PyPDFLoader("./Data/2024_KB_부동산_보고서_최종.pdf")
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return text_splitter.split_documents(documents)

# 벡터DB 초기화
@st.cache_resource
def initialize_vectorstore():
    chunks = process_pdf()
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    return Chroma.from_documents(chunks, embeddings)

# 체인 초기화
@st.cache_resource
def initialize_chain():
    vectorstore = initialize_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    template = """당신은 KB 부동산 보고서 전문가입니다. 다음 정보를 바탕으로 사용자의 질문에 답변해주세요.

    컨텍스트: {context}
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", template),
        ("placeholder", "{chat_history}"),
        ("human", "{question}")
    ])

    model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, openai_api_key=api_key)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    base_chain = (
        RunnablePassthrough.assign(
            context=lambda x: format_docs(retriever.invoke(x["question"]))
        )
        | prompt
        | model
        | StrOutputParser()
    )

    return RunnableWithMessageHistory(
        base_chain,
        lambda session_id: ChatMessageHistory(),
        input_messages_key="question",
        history_messages_key="chat_history",
    )

# Streamlit UI
def main():
    st.set_page_config(page_title="KB 부동산 보고서 챗봇", page_icon="🏠") # 탭 페이지의 제목과 아이콘 설정
    st.title("🏠 KB 부동산 보고서 AI 어드바이저") # 페이지의 제목
    st.caption("2024 KB 부동산 보고서 기반 질의응답 시스템") # 페이지의 부제목

    # 세션 상태 초기화
    if "messages" not in st.session_state: # st.session_state를 사용하여 대화 기록 저장
        st.session_state.messages = []

    # 채팅 기록 표시
    for message in st.session_state.messages:
        with st.chat_message(message["role"]): # st.chat_message을 사용하여 각 메시지를 역할에 따라 구분하여 표시
            st.markdown(message["content"])

    # 사용자 입력 처리
    if prompt := st.chat_input("부동산 관련 질문을 입력하세요"):  # st.chat_input을 사용하여 사용자로부터 입력을 받아
        # 사용자 메시지 표시
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # 체인 초기화
        chain = initialize_chain()

        # AI 응답 생성
        with st.chat_message("assistant"):
            with st.spinner("답변 생성 중..."): # st.spinner를 사용하여 응답을 생성 중임을 표시
                response = chain.invoke(
                    {"question": prompt},
                    {"configurable": {"session_id": "streamlit_session"}}
                )
                st.markdown(response) # st.markdown으로 생성된 응답 표시

        st.session_state.messages.append({"role": "assistant", "content": response}) # 생성된 응답을 세션 상태에 저장하여 대화 기록을 유지

if __name__ == "__main__":
    main()