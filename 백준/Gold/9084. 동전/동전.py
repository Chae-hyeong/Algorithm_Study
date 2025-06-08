import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    coins = list(map(int, input().split()))
    target = int(input())
    dp = [0] * (target + 1)
    dp[0] = 1

    for coin in coins:
        for money in range(target + 1):
            if coin <= money:
                dp[money] += dp[money - coin]

    print(dp[-1])


