# 핸즈온 LLM

『핸즈온 LLM』을 학습하며 핵심 개념과 실습 내용을 정리한 저장소

최근 LLM 기반 서비스에서 널리 사용되는 **RAG(Retrieval-Augmented Generation)**, **Prompt Engineering**, **AI Agent**를 중심으로 학습하며, 책의 예제를 직접 구현하고 관련 개념을 정리

또한 학습한 내용을 기반으로 향후 RAG 및 Agent 프로젝트를 개발하기 위한 기초를 다지는 것이 목표

---

## 학습 기간

- 시작일 : 2026.05.23
- 종료일 : 진행 중

---

## 학습 목표

- Semantic Search와 Dense Retrieval 이해
- RAG 파이프라인 이해
- Prompt Engineering 기법 학습
- Agent의 구조와 Tool Calling 이해
- 예제 코드를 직접 구현하며 실습 경험 축적
- 향후 RAG 및 Agent 프로젝트 개발을 위한 기반 구축

---

## 학습 방법

『핸즈온 LLM』의 모든 챕터를 순차적으로 학습하기보다는 현재 관심 분야인 다음 주제를 우선적으로 학습

- RAG
- Prompt Engineering
- AI Agent

각 챕터를 학습하며 다음 내용을 정리

- 예제 코드 실습
- 코드 내 모르는 함수나 메소드 정리
- 학습하면서 개념 정리

한 챕터 학습이 끝나면 해당 주제를 더 깊게 다루는 전문 서적으로 학습을 이어갈 예정

본 도서는 최근 NLP 트렌드 전반을 빠르게 이해하기 위한 입문서이자 로드맵으로 활용

---

## 진행 상황

| Chapter | Topic | Status |
|----------|----------|----------|
| 06 | 프롬프트 엔지니어링 | ⏳ |
| 07 | 고급 텍스트 생성 기술과 도구 | ⏳ |
| 08 | 시맨틱 검색과 RAG | ✅ [정리](./ch8_RAG.ipynb) <br> [[부록]Sentence-Transformer](./ch8_sentence_transformer.ipynb) |
| 10 | 텍스트 임베딩 모델 만들기 | ⏳ |

---

## 정리 내용

- 챕터별 핵심 개념 정리
- 실습 코드
- 추가 학습 내용


---

## 추후 프로젝트

### Paper Assistant Agent

논문 검색, 요약, 관련 연구 추천 기능을 제공하며,
사용자의 배경지식에 맞는 학습 자료와 커리큘럼을 생성하는 Research Assistant Agent

예상 기술 스택

- BGE-M3
- FAISS
- RAG
- Local LLM (Gemma4)
- LangGraph
---

