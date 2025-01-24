# Transformer 모델

Transformer 모델은 **자연어 처리(NLP)** 및 **시퀀스 데이터 처리**에서 널리 사용되는 딥러닝 모델로, **Self-Attention 메커니즘**을 중심으로 작동합니다. 이 모델은 2017년 Google의 논문 "Attention is All You Need"에서 처음 소개되었습니다.

## 주요 특징
- **Self-Attention 메커니즘**: 시퀀스 내의 모든 단어(토큰)가 서로의 관계를 학습하여 더 나은 문맥 이해를 제공합니다.
- **병렬 처리**: RNN과 달리 순차적 계산에 의존하지 않아 GPU를 활용한 병렬 처리가 가능하며 학습 속도가 빠릅니다.
- **모듈 구조**: Encoder와 Decoder 블록으로 구성되어 있습니다.

---

## 구조

### 1. Encoder
- 입력 데이터를 처리하며, 여러 개의 Encoder 레이어로 구성됩니다.
- 각 레이어는 다음으로 구성됩니다:
  - **Multi-Head Attention**: 입력 토큰 간의 관계를 계산.
  - **Feed Forward Network (FFN)**: 비선형 변환으로 정보를 정제.
  - **Residual Connection & Normalization**: 정보 손실 방지 및 학습 안정성 제공.

### 2. Decoder
- 출력을 생성하는 역할을 하며, Encoder에서 얻은 정보를 활용합니다.
- 각 레이어는 다음으로 구성됩니다:
  - **Masked Multi-Head Attention**: 이전 출력까지만 참조해 출력 생성.
  - **Encoder-Decoder Attention**: Encoder의 정보를 활용.
  - **Feed Forward Network**: 비선형 변환.

---

## 핵심 개념

### 1. Self-Attention
- 시퀀스의 각 단어가 다른 단어들과 상호작용하며 가중치를 계산합니다.
- 주요 공식:  
  \[
  Attention(Q, K, V) = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V
  \]  
  - \( Q \): Query (질의)
  - \( K \): Key (키)
  - \( V \): Value (값)
  - \( d_k \): Key의 차원

### 2. Positional Encoding
- Transformer는 순서를 학습하지 못하므로, 입력 데이터에 위치 정보를 추가하여 순서를 인식하게 만듭니다.

---

## 장점
1. RNN보다 학습 속도가 빠르다.
2. 긴 시퀀스 데이터 처리에 강하다.
3. 병렬화가 용이하다.

## 단점
1. 모델 크기가 크고 학습에 많은 데이터와 자원이 필요하다.
2. Self-Attention 계산 비용이 높다. (O(n²))

---

## 활용 분야
- **자연어 처리**: 번역, 요약, 문장 생성 등
- **컴퓨터 비전**: 이미지 분류, 객체 검출 (Vision Transformer, ViT)
- **음성 처리**: 음성 인식, 합성

---

## 참고 자료
- 논문: [Attention is All You Need](https://arxiv.org/abs/1706.03762)
