MOD = 10**9 + 7

n = int(input())
dp = [[0] * 3 for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n):
    for r in range(3):
        dp[i + 1][(r + 1) % 3] = (dp[i + 1][(r + 1) % 3] + dp[i][r]) % MOD
        dp[i + 1][(r + 5) % 3] = (dp[i + 1][(r + 5) % 3] + dp[i][r]) % MOD

print(dp[n - 1][1] % MOD)