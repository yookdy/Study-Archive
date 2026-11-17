import torch
import torch.nn as nn
import torch.nn.functional as F

def pratice_self_attention():
    torch.manual_seed(42) # 난수 시드 설정 (재현성을 위해)

    x=torch.tensor([[[1.0, 0.0, 1.0, 0.0],
                    [0.0, 2.0, 0.0, 1.0],
                    [1.0, 1.0, 0.0, 0.0]]])

    print(f"1. 입력 텐서 (Shape: {x.shape}):\n{x}\n")\


    seq_len, d_in = x.shape[1], x.shape[2] #배치 크기 1, 시퀀스 길이 3, 입력 차원 4
    #배치 크기: 한번에 동시 처리하는 문장 묶음 수 --> 하나의 행렬을 하나의 문장으로 생각
    #시퀀스 길이: 문장의 단어(토큰)의 수 --> 예시에서 행이 3개로 시퀀스는 3개
    #입력 차원: 단어 하나를 표현하는 벡터의 개수 --> 예시 하나의 단어를 구성하는 숫자가 4개
    d_out = 4

    W_query = nn.Linear(d_in, d_out, bias = False) #질문 
    W_key = nn.Linear(d_in, d_out, bias = False)  #열쇠 입력데이터를 key로 변환
    W_value = nn.Linear(d_in, d_out, bias = False)  #정보 실제 정보가 담긴 벡터로 전환

    Q = W_query(x)
    K = W_key(x)
    V = W_value(x)

    print(f"Query 형태: {Q.shape}")
    print(f"Key 형태: {K.shape}")
    print(f"Value 형태: {V.shape}\n")

    attention_scores = torch.matmul(Q, K.transpose(1,2)) # key를 전치함 
    print(f"4. 어텐션 스코어 (Shape: {attention_scores.shape}):\n{attention_scores}\n")

    d_k =Q.shape[-1]
    scaled_attention_scores = attention_scores / (d_k ** 0.5) 
    #차원의 크기가 커질수록 어텐션 점수 값도 무지막지하게 커져서 뒤에서 확률 계산 시 기울기 소실 문제가 생기는 것을 막기 위해,
    #차원 크기의 제곱근(√d_k)으로 점수들을 나눠 스케일을 안정적으로 낮춰줍니다.

    #스케일링된 점수들을 F.softmax에 통과시켜, 각 단어가 다른 단어들을 향하는 어텐션 가중치의 비율로 변환
    attention_weights = F.softmax(scaled_attention_scores, dim=-1)
    print(f"5. 어텐션 가중치 확률 (Softmax 통과 후):\n{attention_weights}\n")

    #어텐션 가중치(확률)와 실제 정보가 담긴 Value($V$) 텐서를 행렬 곱셈
    context_vector = torch.matmul(attention_weights, V)
    print(f"6. 최종 어텐션 결과 Context Vector (Shape: {context_vector.shape}):\n{context_vector}")

if __name__ =="__main__":
    pratice_self_attention()