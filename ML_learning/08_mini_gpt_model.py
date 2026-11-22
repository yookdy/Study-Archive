import math
import torch
import torch.nn as nn
import torch.nn.functional as F


class MultiHeadAttention(nn.Module):
    def __init__(self, embed_dim, num_heads): #기본적인 어텐션 계산을 수행하는 모듈
        super().__init__()
        assert (
            embed_dim % num_heads == 0
        ), "embed_dim은 num_heads로 나누어떨어져야 합니다."

        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads

        self.q_linear = nn.Linear(embed_dim, embed_dim)
        self.k_linear = nn.Linear(embed_dim, embed_dim)
        self.v_linear = nn.Linear(embed_dim, embed_dim)
        self.out_linear = nn.Linear(embed_dim, embed_dim)

    def forward(self, x):
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
    def __init__(self, embed_dim, ff_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(embed_dim, ff_dim),
            nn.ReLU(),
            nn.Linear(ff_dim, embed_dim),
        )

    def forward(self, x):
        return self.net(x)


class TransformerBlock(nn.Module): #트랜스포머 블록을 구성하는 핵심 모듈
    def __init__(self, embed_dim, num_heads, ff_dim):
        super().__init__()
        self.attention = MultiHeadAttention(embed_dim, num_heads)
        self.norm1 = nn.LayerNorm(embed_dim)
        self.ffn = FeedForward(embed_dim, ff_dim)
        self.norm2 = nn.LayerNorm(embed_dim)

    def forward(self, x):
        attn_out, _ = self.attention(x)
        x = self.norm1(x + attn_out)
        ffn_out = self.ffn(x)
        x = self.norm2(x + ffn_out)
        return x


class MiniGPT(nn.Module): #트랜스포머 블록을 쌓아 LLM을 구성하는 미니 GPT 모델
    """임베딩 + 위치 인코딩 + 트랜스포머 블록 스택 + 다음 단어 예측기를 결합한 미니 LLM"""
    def __init__(self, vocab_size, max_seq_len, embed_dim, num_heads, ff_dim, num_layers):
        super().__init__()
        # 1. 단어 의미 임베딩 & 단어 위치(순서) 임베딩
        self.token_embedding = nn.Embedding(vocab_size, embed_dim)
        self.position_embedding = nn.Embedding(max_seq_len, embed_dim)

        # 2. 트랜스포머 블록을 num_layers 개수만큼 층층이 쌓기
        self.blocks = nn.ModuleList(
            [TransformerBlock(embed_dim, num_heads, ff_dim) for _ in range(num_layers)]
        )

        # 3. 최종 정규화 및 단어 사전 크기(vocab_size)로 변환하는 출력 헤드(LM Head)
        self.final_norm = nn.LayerNorm(embed_dim)
        self.lm_head = nn.Linear(embed_dim, vocab_size)

    def forward(self, input_ids):
        # input_ids shape: (batch_size, seq_len)
        batch_size, seq_len = input_ids.shape

        # 0부터 seq_len-1까지의 위치 인덱스 생성: [0, 1, 2]
        positions = torch.arange(0, seq_len, device=input_ids.device).unsqueeze(0)

        # 단어 의미 벡터 + 위치 순서 벡터 결합
        x = self.token_embedding(input_ids) + self.position_embedding(positions)

        # 쌓아 올린 트랜스포머 블록들을 순서대로 통과
        for block in self.blocks:
            x = block(x)

        x = self.final_norm(x)

        # 각 위치별로 전체 단어 사전(vocab_size)에 대한 예측 점수(Logits) 산출
        logits = self.lm_head(x)
        return logits


if __name__ == "__main__":
    torch.manual_seed(42)

    # 하이퍼파라미터 설정
    vocab_size = 10     # 단어 사전 크기 (0~9번 토큰)
    max_seq_len = 16    # 모델이 처리할 수 있는 최대 문장 길이
    embed_dim = 8       # 임베딩 차원
    num_heads = 2       # 어텐션 헤드 수
    ff_dim = 32         # FFN 확장 차원
    num_layers = 2      # 트랜스포머 블록을 2층으로 쌓음

    model = MiniGPT(vocab_size, max_seq_len, embed_dim, num_heads, ff_dim, num_layers)

    # 가상의 입력 문장 (토큰 ID: [1, 4, 7])
    input_ids = torch.tensor([[1, 4, 7]])

    # 순전파 실행
    logits = model(input_ids)

    # 마지막 단어(7번 토큰) 다음에 올 단어의 확률 계산
    last_token_logits = logits[:, -1, :]               # shape: [1, 10]
    probs = F.softmax(last_token_logits, dim=-1)       # 10개 단어별 확률 분포
    predicted_token_id = torch.argmax(probs, dim=-1)   # 가장 확률이 높은 토큰 ID 선택

    print(f"입력 토큰 ID 형태 (Input Shape): {input_ids.shape}")
    print(f"전체 출력 Logits 형태 (Logits Shape): {logits.shape}")
    print(f"다음 단어 확률 분포 (Probs): {probs.detach()}")
    print(f"예측된 다음 토큰 ID: {predicted_token_id.item()}")