# RAG 마스터: 랭체인으로 완성하는 LLM 서비스

『RAG 마스터: 랭체인으로 완성하는 LLM 서비스』를 학습하며 RAG(Retrieval-Augmented Generation)의 핵심 개념과 실습 내용을 정리한 저장소입니다.

기본적인 RAG 파이프라인부터 Multimodal RAG, Graph RAG, Agentic RAG, RAG 성능 최적화 기법까지 학습하며, 예제 코드를 직접 구현하고 관련 개념을 정리합니다.

또한 학습한 내용을 기반으로 향후 RAG 기반 서비스를 개발하기 위한 기반을 다지는 것을 목표로 합니다.

---

## 학습 기간

- 시작일 : 2026.05.26
- 종료일 : 진행 중

---

## 학습 목표

- LangChain 기반 RAG 구현 방법 이해
- RAG 파이프라인 설계 및 최적화 기법 학습
- Chunking, Embedding, Retrieval, Reranking 이해
- Multimodal RAG 구현 방법 이해
- Graph RAG 개념 및 활용 방법 학습
- LangGraph를 활용한 Agentic RAG 구현
- LLM 및 Embedding 모델 파인튜닝을 통한 RAG 성능 개선 방법 학습
- 향후 RAG 및 Agent 프로젝트 개발을 위한 기반 구축

---

## 학습 방법

『RAG 마스터: 랭체인으로 완성하는 LLM 서비스』의 모든 챕터를 순차적으로 학습하기보다는 현재 관심 분야인 다음 주제를 우선적으로 학습

- RAG 기초
- RAG 고도화
- Agentic RAG

각 챕터를 학습하며 다음 내용을 정리

- 예제 코드 실습
- 코드 내 모르는 함수나 메소드 정리
- 학습하면서 개념 정리


---

## 진행 상황

| Chapter | Topic | Status |
|----------|----------|----------|
| 01 | 랭체인 살펴보기 | [✅](./ch1.ipynb) |
| 02 | 검색 증강 생성 기초와 실습 | [✅](./ch2.ipynb), [✅](./chatbot.py) |
| 03 | 멀티모달 RAG를 활용한 복합 데이터 처리 |⏳|
| 04 | 검색과 응답을 최적화하는 RAG 고도화 전략 | [✅](./ch4.ipynb) |
| 05 | 지식 그래프를 활용한 그래프 RAG | ⏳ |
| 06 | 랭그래프로 설계하는 RAG 파이프라인 | ⏳ |
| 07 | 리액트 에이전트를 활용한 RAG |  [✅](./ch7.ipynb) |
| 08 | RAG 성능을 높이는 LLM 파인튜닝 | ⏳ |
| 09 | 임베딩 모델 파인튜닝 | ⏳ |

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
- Reranker
- LangChain
- LangGraph
- Local LLM (Gemma4)
---

