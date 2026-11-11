import torch
import torch.nn as nn

class SimpleNetwork(nn. Module):

    def __init__(self): # 모델 초기화
        super().__init__()
        # 선형 계층 정의 (입력 특성 3개, 출력 특성 2개)
        self.linear_layer = nn.Linear(in_features = 3, out_features = 2)
        # ReLU 활성화 함수 정의 비선형 함수
        self.relu = nn.ReLU()

    def forward(self, x): # 모델의 순전파 정의

        out = self.linear_layer(x) # 선형 계층에 입력 데이터 통과
        print(f"선형 계층 출력: {out.detach()}")

        out = self.relu(out) # ReLU 활성화 함수 적용
        print(f"ReLU 활성화 함수 출력: {out.detach()}")

        return out

if __name__ =="__main__":
    # 랜덤 시드 설정 (재현성을 위해)
    torch.manual_seed(42)

    # 모델 생성
    model = SimpleNetwork()

    print("모델 내부의 가중치(Weight)와 편향(Bias):")
    print(model.linear_layer.weight)
    print(model.linear_layer.bias, "\n")

    # 입력 데이터 생성 (2개의 샘플, 각 샘플은 3개의 특성)
    input_data = torch.tensor([[1.0, 2.0, 3.0], 
                                   [4.0, 5.0, 6.0]])

    print(f"입력 데이터 (Shape: {input_data.shape}):\n{input_data}\n")

    # 데이터를 모델에 통과시키기 (자동으로 forward 함수가 실행됨)
    print(f"모델 출력 (Shape: {input_data.shape}):\n{input_data}\n")
    print("--- 모델에 데이터 통과 시작 ---")

    #forward 함수 호출 -->model(input_data)로 호출하면 nn>Module의 forward()가 자동으로 호출됨
    #__call__() 매서드가 알아서 찾아감
    output = model(input_data)


