import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

S = set()
count = 0

for _ in range(N):
  S.add(input().rstrip())

for _ in range(M):
  if input().rstrip() in S:
    count += 1

print(count)