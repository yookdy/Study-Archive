import torch #수학 계산 도구 라이브러리

#tensor: 다차원 배열을 나타내는 자료구조 ->계산이 GPU에서 빠르게 수행될 수 있도록 최적화되어 있음
def practice_tensor_basics():
    data = [[1,2], [3,4]]
    tensor = torch.tensor(data, dtype = torch.float32)
    print("1. 기본 텐서 생성: ")
    print(tensor)
    print(f" 차원(Dim): {tensor.ndim}D, 형태(Shape): {tensor.shape}\n")

    # 2행 3열짜리 텐서를 새로 만듬
    # 초가 가중치 역활
    rand_tensor = torch.rand(2, 3)
    print("2. 난수 텐서(초기 가중치):")
    print(rand_tensor)
    print(f"형태(Shape): {rand_tensor.shape}\n")

    # 3행 2열로 형태 변경
    # 데이터 형태에 따른 변경하는 방법
    reshaped_tensor = rand_tensor.view(3, 2)
    print("3. 형태 변경된 텐서 (2x3 -> 3x2):")
    print(reshaped_tensor)
    print(f"형태(Shape): {reshaped_tensor.shape}\n")

    tensor_a = torch.tensor([[1, 2], [3, 4]])
    tensor_b = torch.tensor([[5, 6], [7, 8]])

    matmul_result = torch.matmul(tensor_a, tensor_b)
    
    print("4. 행렬 곱셈 연산 결과:")
    print(f"A:\n{tensor_a}")
    print(f"B:\n{tensor_b}")
    print(f"A @ B 결과:\n{matmul_result}\n")


if __name__ == "__main__":
    practice_tensor_basics()