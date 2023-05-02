import re

with open('3.10.txt', 'r') as f:
    text = f.read()

sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
num_sentences = len(sentences)

print("Number of sentences:", num_sentences)
