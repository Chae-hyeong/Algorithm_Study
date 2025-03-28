
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1)

for weight, value in items:
    for k in range(K, weight - 1, -1):
        dp[k] = max(dp[k], dp[k - weight] + value)

print(dp[K])