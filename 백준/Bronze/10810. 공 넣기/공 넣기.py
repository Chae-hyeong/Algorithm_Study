import sys
input = sys.stdin.readline

N, M = map(int, input().split())
answer = [0 for _ in range(N)]

for _ in range(M):
    i, j, k = map(int, input().split())
    answer[i-1:j] = [k] * (j - i + 1)

print(*answer)