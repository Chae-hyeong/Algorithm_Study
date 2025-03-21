import sys
from collections import deque

input = sys.stdin.readline

K = int(input())

q = deque(int(input()) for _ in range(K))
answer = []

while q:
    num = q.popleft()
    if num == 0:
        answer.pop()
    else:
        answer.append(num)


print(sum(answer))

