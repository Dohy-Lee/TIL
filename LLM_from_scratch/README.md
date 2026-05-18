# 밑바닥부터 만들면서 배우는 LLM

학습 날짜: 2026.05.04 ~ 2026.05.19

LLM의 내부 구조를 이해하기 위해 『밑바닥부터 만들면서 배우는 LLM』을 학습하며 정리한 저장소

석사과정 동안 트랜스포머 인코더 기반의 BERT를 중심으로 연구 및 실험을 진행했기 때문에,  
디코더 기반 LLM 아키텍처에 대한 이해를 보완하고자 이 책을 학습함

토큰화부터 Self-Attention, GPT 구현, 사전학습, 파인튜닝까지 직접 따라가며  
LLM이 텍스트를 처리하고 생성하는 전체 흐름을 이해하는 것을 목표로 하였음

## 학습 목표

- 디코더 기반 Transformer 구조 이해
- GPT 모델의 주요 구성 요소 직접 구현
- 토큰화와 임베딩 과정 이해
- Self-Attention 및 Multi-Head Attention 동작 방식 이해
- 사전학습과 파인튜닝의 차이 이해
- 분류 파인튜닝과 지시 파인튜닝의 흐름 이해
- 이후 Hugging Face Transformers, RAG, AI Agent 학습을 위한 기반 다지기

## 정리 내용

- 각 챕터의 핵심 개념 요약
- 직접 구현한 코드 정리
- 실습 중 헷갈렸던 부분 기록


## Chapter

| Chapter | Topic | Link |
|---|---|---|
| 01 | LLM 개요 | 
| 02 | 텍스트 데이터 다루기 | [정리](./chapters/ch02-tokenization.md) |
| 03 | 어텐션 메커니즘 | [정리](./chapters/ch03-attention.md) |
| 04 | GPT 모델 구현 | [정리](./chapters/ch04-gpt-implementation.md) |
| 05 | 사전학습 | [정리](./chapters/ch05-pretraining.md) |
| 06 | 분류 파인튜닝 | [정리](./chapters/ch06-classification-finetuning.md) |
| 07 | 지시 파인튜닝 | [정리](./chapters/ch07-instruction-finetuning.md) |
