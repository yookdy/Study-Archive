import math
import torch
import torch.nn as nn
import torch.nn.functional as F


class MultiHeadAttention(nn.Module):
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        assert(
            embed_dim % num_heads == 0
        ), "embed_dim은 num_heads로 나누어떨어져야 합니다."

        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads

        self.q_linear = nn.Linear(embed_dim, embed_dim)
        self.k_linear = nn.Linear(embed_dim, embed_dim)
        self.v_linear = nn.Linear(embed_dim, embed_dim) 
        self.out_linear = nn.Linear(embed_dim, embed_dim)


    def forward(self, x): # 어텐션 계산 수행
        batch_size, seq_len, _ = x.shape
        
        Q = self.q_linear(x)
        K = self.k_linear(x)
        V = self.v_linear(x)

        Q = Q.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        K = K.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        V = V.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)

        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.head_dim)
        attention_weights = F.softmax(scores, dim=-1)

        context = torch.matmul(attention_weights, V)

        context = (
            context.transpose(1, 2)
            .contiguous()
            .view(batch_size, seq_len, self.embed_dim)
        )

        output = self.out_linear(context)
        return output, attention_weights

class FeedForward(nn.Module): #주변 단어와의 연관성 심화
    '''어텐션이 수집한 문맥 정보를 바탕으로 각 단어를 독립적으로 심화 학습하는 신경망'''
    def __init__(self, embed_dim, ff_dim):
        super().__init__()
        self.net = nn.Sequential(
            # 8-->32--> 8 차원 변환
            nn.Linear(embed_dim, ff_dim), # 원본 임베딩 차원을 확장된 차원으로 변환 
            nn.ReLU(), # 음수 값 제거
            nn.Linear(ff_dim, embed_dim) 
        )
    def forward(self, x):
        return self.net(x)

class TransformerBlock(nn.Module): #
    """LLM을 구성하는 핵심 단위 블록 (MHA + Add & Norm + FFN + Add & Norm)"""
    def __init__(self, embed_dim, num_heads, ff_dim):
        super().__init__()
        #문맥을 파악하는 어텐션 엔진과 지식을 가공하는 신경망 엔진 장착
        self.attention = MultiHeadAttention(embed_dim, num_heads) #--> attention은 MultiHeadAttention 클래스의 인스턴스
        self.ffn = FeedForward(embed_dim, ff_dim)
        # norm1, norm2: 평균을 0, 표준편차를 1로 강제 정렬하여 졍규화해서 학습 안정화
        self.norm1 = nn.LayerNorm(embed_dim)
        self.norm2 = nn.LayerNorm(embed_dim)

    def forward(self, x):
        # 1. 멀티 헤드 어텐션 + 잔차 연결(x + attn_out) + 층 정규화(norm1)
        attn_out, attn_weights = self.attention(x)
        x = self.norm1(x + attn_out) #원본 단어뜻 + 주변단어 연관성 식으로 보존

        # 2. 피드포워드 신경망 + 잔차 연결(x + ffn_out) + 층 정규화(norm2)
        ffn_out = self.ffn(x)
        x = self.norm2(x + ffn_out)

        return x, attn_weights

if __name__ == "__main__":
    batch_size = 1  # 배치 크기: 한 번에 처리하는 문장 묶음 수
    seq_len = 3
    embed_dim = 8
    num_heads = 2
    ff_dim = 16 # FFN 확장 차원 (보통 embed_dim의 4배) --> 연관성을 더 깊게 학습하기 위해 확장된 차원으로 피드포워드 신경망을 구성

    x = torch.randn(batch_size, seq_len, embed_dim)
    transformer_block = TransformerBlock(embed_dim, num_heads, ff_dim)

    output = transformer_block(x)
    output, attn_weights = transformer_block(x)
    print(f"입력 텐서 형태 (Input Shape): {x.shape}")
    print(f"트랜스포머 블록 통과 후 출력 형태 (Output Shape): {output.shape}")
    print("\n--- 블록 통과 후 최종 출력 텐서 일부 ---")
    print(output.detach())

    '''
    어텐션(MHA): "주변 단어들과 어떤 관계지?" (문맥 수집)
    더하기 & 정규화(Add & Norm): "원래 내 뜻도 잊지 말고 숫자 크기 맞추자!"
    피드포워드(FFN): "수집한 문맥을 바탕으로 깊게 생각해 보자!" (8 -> 32 -> 8)
    더하기 & 정규화(Add & Norm): "방금 생각한 내용에 기존 정보 더하고 깔끔하게 정리하자!" 
    최종 출력 ([1, 3, 8]): 다음 트랜스포머 층으로 올라갈 준비 완료!
    '''