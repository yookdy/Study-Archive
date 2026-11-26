import math
import torch
import torch.nn as nn
import torch.nn.functional as F


class CausalMultiHeadAttention(nn.Module):
    """미래 토큰을 미리 보지 못하도록 마스킹(Causal Mask)이 적용된 멀티 헤드 어텐션"""
    def __init__(self, embed_dim, num_heads, max_seq_len):
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

        # 하삼각 행렬(1로 채워진 왼쪽 아래 삼각형)을 만들어 버퍼로 등록
        # 위쪽 삼각형(미래 위치)은 0이 되어 마스킹 대상으로 사용됩니다.
        mask = torch.tril(torch.ones(max_seq_len, max_seq_len))
        self.register_buffer("mask", mask)

    def forward(self, x):
        batch_size, seq_len, _ = x.shape

        Q = self.q_linear(x)
        K = self.k_linear(x)
        V = self.v_linear(x)

        Q = Q.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        K = K.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        V = V.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)

        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.head_dim)

        # 현재 문장 길이(seq_len)만큼 마스크를 자른 뒤, 0인 위치(미래 단어)를 -inf(음의 무한대)로 채움
        scores = scores.masked_fill(
            self.mask[:seq_len, :seq_len] == 0, float("-inf")
        )

        # -inf에 softmax를 취하면 확률이 정확히 0.0이 되어 미래 단어 정보가 완벽히 차단됨
        attention_weights = F.softmax(scores, dim=-1)
        context = torch.matmul(attention_weights, V)

        context = (
            context.transpose(1, 2)
            .contiguous()
            .view(batch_size, seq_len, self.embed_dim)
        )
        output = self.out_linear(context)
        return output, attention_weights


class FeedForward(nn.Module):
    def __init__(self, embed_dim, ff_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(embed_dim, ff_dim),
            nn.ReLU(),
            nn.Linear(ff_dim, embed_dim),
        )

    def forward(self, x):
        return self.net(x)


class TransformerBlock(nn.Module):
    def __init__(self, embed_dim, num_heads, ff_dim, max_seq_len):
        super().__init__()
        self.attention = CausalMultiHeadAttention(embed_dim, num_heads, max_seq_len)
        self.norm1 = nn.LayerNorm(embed_dim)
        self.ffn = FeedForward(embed_dim, ff_dim)
        self.norm2 = nn.LayerNorm(embed_dim)

    def forward(self, x):
        attn_out, attn_weights = self.attention(x)
        x = self.norm1(x + attn_out)
        ffn_out = self.ffn(x)
        x = self.norm2(x + ffn_out)
        return x, attn_weights


class CausalMiniGPT(nn.Module):
    """인과적 마스킹과 자기회귀(Autoregressive) 문장 생성 기능을 갖춘 GPT 모델"""
    def __init__(self, vocab_size, max_seq_len, embed_dim, num_heads, ff_dim, num_layers):
        super().__init__()
        self.max_seq_len = max_seq_len
        self.token_embedding = nn.Embedding(vocab_size, embed_dim)
        self.position_embedding = nn.Embedding(max_seq_len, embed_dim)

        self.blocks = nn.ModuleList(
            [
                TransformerBlock(embed_dim, num_heads, ff_dim, max_seq_len)
                for _ in range(num_layers)
            ]
        )

        self.final_norm = nn.LayerNorm(embed_dim)
        self.lm_head = nn.Linear(embed_dim, vocab_size)

    def forward(self, input_ids):
        batch_size, seq_len = input_ids.shape
        positions = torch.arange(0, seq_len, device=input_ids.device).unsqueeze(0)

        x = self.token_embedding(input_ids) + self.position_embedding(positions)

        attn_weights = None
        for block in self.blocks:
            x, attn_weights = block(x)

        x = self.final_norm(x)
        logits = self.lm_head(x)
        return logits, attn_weights

    @torch.no_grad() #문장 학습 중에는 가중치 업데이트를 하지 않도록 설정
    # 상삼각으로 행렬을 전환하여 미래 단어를 보지 못하도록 마스킹
    def generate(self, input_ids, max_new_tokens):
        """기존 입력 뒤에 새로운 토큰을 한 개씩 반복해서 이어 붙이는 생성 함수"""
        for _ in range(max_new_tokens):
            # 최대 문장 길이(max_seq_len)를 넘지 않도록 뒤에서부터 자르기
            idx_cond = input_ids[:, -self.max_seq_len :]

            logits, _ = self(idx_cond)
            last_token_logits = logits[:, -1, :]
            probs = F.softmax(last_token_logits, dim=-1)
            next_token = torch.argmax(probs, dim=-1, keepdim=True)

            # 예측한 토큰을 기존 문장 뒤에 이어 붙이기 (Concat)
            input_ids = torch.cat((input_ids, next_token), dim=1)

        return input_ids


if __name__ == "__main__":
    torch.manual_seed(42)

    vocab_size = 10
    max_seq_len = 16
    embed_dim = 8
    num_heads = 2
    ff_dim = 32
    num_layers = 2

    model = CausalMiniGPT(vocab_size, max_seq_len, embed_dim, num_heads, ff_dim, num_layers)

    # 초기 입력 문장: [1, 4, 7]
    input_ids = torch.tensor([[1, 4, 7]])

    # 1. 마스킹된 어텐션 가중치 확인
    _, attn_weights = model(input_ids)
    print("--- 인과적 마스크(Causal Mask)가 적용된 어텐션 가중치 (Head 0) ---")
    print(attn_weights[0, 0])

    # 2. 다음 토큰 4개를 연속으로 생성(Autoregressive Generation)
    generated_ids = model.generate(input_ids, max_new_tokens=4)
    print(f"\n초기 입력 토큰: {input_ids.tolist()}")
    print(f"4개 토큰 연속 생성 결과: {generated_ids.tolist()}")