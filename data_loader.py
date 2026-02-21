import re
from SimpleTokenizerV1 import SimpleTokenizerV1

file_path = "the-verdict.txt"
with open(file_path, "r", encoding="utf-8") as f:
    raw_text = f.read()

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s+)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
all_words = sorted(set(preprocessed))
vocab = {word: idx for idx, word in enumerate(all_words)}
tokenizer = SimpleTokenizerV1(vocab)
ids = tokenizer.encode(raw_text)
print(tokenizer.decode(ids)) 
