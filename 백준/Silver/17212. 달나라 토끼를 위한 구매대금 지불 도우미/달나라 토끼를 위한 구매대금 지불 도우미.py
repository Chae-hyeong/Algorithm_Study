N = int(input())
coins = [1, 2, 5, 7]

dp = [float('inf')] * (N + 1)
dp[0] = 0

for i in range(1, N + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[N])