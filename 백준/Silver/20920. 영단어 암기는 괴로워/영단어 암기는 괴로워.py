import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())
words = [input().strip() for _ in range(n)]

counter = Counter(words)

filtered_words = [(word, len(word), count) for word, count in counter.items() if len(word) >= m]

sorted_words = sorted(filtered_words, key=lambda x: (-x[2], -x[1], x[0]))

for word, _, _ in sorted_words:
    print(word)