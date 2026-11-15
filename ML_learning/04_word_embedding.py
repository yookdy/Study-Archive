import torch
import torch.nn as nn


def pratice_embedding():
    torch.manual_seed(42)

    #1. 임베딩 레이어 정의 (단어 수: 10, 임베딩 차원: 5)
    # 단어장의 총 크기(vocab_size)는 10개로 가정하고,
    # 각 단어를 4개의 실수(embedding_dim)로 이루어진 벡터로 표현합니다.
    vocab_size = 10
    embedding_dim = 5
    # 10행 5열 임의의 가중치 행렬 생성
    embedding_layer = nn.Embedding(num_embeddings=vocab_size, embedding_dim = embedding_dim)

    print("1. 임베딩 계층 내부의 가중치 행렬 (Lookup Table):")
    # 0번부터 9번까지 10개의 단어가 각각 4차원 벡터로 무작위 초기화되어 있습니다.
    print(embedding_layer.weight.detach())
    print(f"형태(Shape): {embedding_layer.weight.shape}\n")

    input_ids = torch.tensor([[1,2,3],[0,4,1]])
    print(f"2. 입력 단어 ID 텐서 (Shape: {input_ids.shape}):\n{input_ids}\n")

    # 3. 단어 ID를 의미를 가진 밀집 벡터(Dense Vector)로 변환
    embedded_output = embedding_layer(input_ids)

    print("3. 임베딩 계층 통과 후 변환된 결과:")
    print(f"결과 형태(Shape): {embedded_output.shape}\n")
    print(embedded_output.detach())
    
    print("\n[핵심 원리]")
    print("출력된 텐서의 첫 번째 묶음을 보면, 입력 ID '1'에 해당하는 벡터가")
    print("맨 위 1번 단계에서 출력된 전체 가중치 행렬의 1번 인덱스(두 번째 줄) 값을")
    print("복사해서 그대로 가져온 것을 확인할 수 있습니다.")


if __name__ == "__main__":
    pratice_embedding()