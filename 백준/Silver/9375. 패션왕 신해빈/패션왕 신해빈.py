import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    wear = [input().split()[1] for _ in range(n)]

    wear_counter = Counter(wear)
    cnt = 1

    for key in wear_counter:
        cnt *= wear_counter[key] + 1

    print(cnt - 1)