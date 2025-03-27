import sys
import bisect

input = sys.stdin.readline

N = int(input())
info = [tuple(map(int, input().split())) for _ in range(N)]

info.sort(key=lambda x: x[1])

end_times = [end for _, end, _ in info]

dp = [0] * (N + 1)

for i in range(1, N + 1):
    start, end, people = info[i - 1]

    j = bisect.bisect_right(end_times, start - 1)

    dp[i] = max(dp[i - 1], dp[j] + people)

print(dp[N])