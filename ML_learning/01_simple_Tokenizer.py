import re 
from collections import Counter

class SimpleTokenizer:
    def __init__(self):
        self.vocab = {}  #단어장
        self.inverse_vocab = {} #들어가는 방향의 역방향 단어장

    def train(self, text):
        # 1. 정규식을 사용해 단어와 특수문자 분리
        tokens = re.findall(r'\b\w+\b|[^\w\s]', text.lower())

        # 2. 단어 빈도수 계산
        word_counts = Counter(tokens)

        # 3. 특수 토큰 추가 (LLM에서 모르는 단어를 처리하는 UNK 토큰)
        self.vocab['<UNK>'] = 0 # 단어장의 0번째는 unknown token으로 설정

        # 4. 고유 단어들에 고유한 정수 ID 부여
        idx = 1 #실제 단어 ID는 1부터 시작
        for word, _ in word_counts.most_common():
            if word not in self.vocab:
                self.vocab[word] = idx
                idx += 1

        self.inverse_vocab = {v: k for k, v in self.vocab.items()}
        
    def encode(self, text):
        """텍스트를 토큰 ID 리스트로 변환"""
        tokens = re.findall(r'\b\w+\b|[^\w\s]', text.lower())
        return [self.vocab.get(token, self.vocab['<UNK>']) for token in tokens]
    
    def decode(self, token_ids):
        """토큰 ID 리스트를 다시 텍스트로 변환"""
        return ' '.join([self.inverse_vocab.get(token_id, '<UNK>') for token_id in token_ids])


if __name__ == "__main__":
    corpus = "Hello world! Building a personal LLM is fun. Hello AI."
    tokenizer = SimpleTokenizer()
    tokenizer.train(corpus)

    print(f"단어 사전(Vocab) 크기: {len(tokenizer.vocab)}")
    print(f"단어 사전: {tokenizer.vocab}\n")

    test_sentence = "Hello LLM world! This is new."
    encoded  =tokenizer.encode(test_sentence)
    decoded = tokenizer.decode(encoded)

    print(f"테스트 문장: '{test_sentence}'")
    print(f"인코딩 결과(Token IDs): {encoded}")
    print(f"디코딩 결과(Text): '{decoded}'")



