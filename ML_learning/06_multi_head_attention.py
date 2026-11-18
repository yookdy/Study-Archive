import math
import torch
import torch.nn as nn
import torch.nn.functional as F

class MultiHeadAttention(nn.Module):
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        assert (
            embed_dim % num_heads == 0
        ), "embed_dim은 num_heads로 나누어떨어져야 합니다." #차원이 2개로 분리되어야 함

        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads

        #q, k, v를 각각으로 8차원으로 나누어 2개의 헤드로 쪼갬
        self.q_linear = nn.Linear(embed_dim, embed_dim)
        self.k_linear = nn.Linear(embed_dim, embed_dim)
        self.v_linear = nn.Linear(embed_dim, embed_dim)


        self.out_linear = nn.Linear(embed_dim, embed_dim)

    def forward(self, x):
        batch_size, seq_len, _ = x.shape # x.shape: 입력 텐서 x의 크기 -> 먼저 형식을 지정하는 역활

        #가중치 행렬이 곱해서 [1,3,8]로 만듬
        Q = self.q_linear(x) 
        K = self.k_linear(x)
        V = self.v_linear(x)

        #[1, 3, 2, 4] 형태로 전환 ---> .transpose(1, 2)로 [1, 2, 3, 4]로 전환(축 교환)
        Q = Q.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2) 
        K = K.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        V = V.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)


        #$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$ 식으로 전환
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.head_dim) # transpose(-2, -1)로 [1, 2, 3, 4] ->[1, 2, 4, 3])
        # --> 계산된 점수를 헤드 차원 수의 제곱근으로 전환 -> head-dim의 크기 조정
        attention_weights = F.softmax(scores, dim=-1)
        # --> 실질적인 비율로 연관성 계산

        #확정된 집중 비율(attention_weights)대로 실제 단어의 의미 내용(V)을 섞어서 최종 문맥 벡터
        context = torch.matmul(attention_weights, V)

        context = (
            context.transpose(1, 2)
            .contiguous()
            .view(batch_size, seq_len, self.embed_dim)
        )# --> [1, 2, 3, 4] -> [1, 3, 2, 4] -> [1, 3, 8]로 전환 원랴 형식으로 전환

        output = self.out_linear(context)
        return output, attention_weights


if __name__ == "__main__":
    torch.manual_seed(42)

    batch_size = 1  # 문장 1개
    seq_len = 3     # 단어 3개
    embed_dim = 8   # 각 단어를 8개의 숫자로 표현 --> 임베딩 차원
    num_heads = 2   # 멀티헤드 어텐션에서 헤드 수 2개 --> 문장을 2개로 쪼갬

    x = torch.randn(batch_size, seq_len, embed_dim) #x로 전달
    mha = MultiHeadAttention(embed_dim, num_heads)
    output, attn_weights = mha(x)

    print(f"입력 텐서 형태 (Input Shape): {x.shape}")
    print(f"어텐션 가중치 형태 (Weights Shape): {attn_weights.shape}")
    print(f"최종 출력 형태 (Output Shape): {output.shape}")
    print("\n--- 헤드별 어텐션 가중치 (단어 간 연관도) ---")
    print(attn_weights.detach())
    
