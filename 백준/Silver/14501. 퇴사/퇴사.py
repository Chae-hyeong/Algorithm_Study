import sys
input = sys.stdin.readline

n = int(input())
arr = [[0, 0]]
for _ in range(n):
    arr.append(list(map(int, input().split())))

dp = [0 for _ in range(n+1)]

for i in range(n+1):
    if i + arr[i][0] > n+1:
        arr[i][1] = 0

for i in range(n):
    for j in range(i+arr[i][0], n+1):
        if dp[j] < dp[i] + arr[j][1]:
            dp[j] = dp[i] + arr[j][1]

print(max(dp))