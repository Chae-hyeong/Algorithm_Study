import sys
input = sys.stdin.readline

# 입력
N = int(input())
first_row = list(map(int, input().split()))

# dp 배열
max_dp = first_row[:]
min_dp = first_row[:]

for _ in range(N-1):
    a, b ,c = map(int, input().split())

    new_max = [0] * 3
    new_min = [0] * 3

    # 최댓값 갱신
    new_max[0] = max(max_dp[0], max_dp[1]) + a
    new_max[1] = max(max_dp[0], max_dp[1], max_dp[2]) + b
    new_max[2] = max(max_dp[1], max_dp[2]) + c

    # 최솟값 갱신
    new_min[0] = min(min_dp[0], min_dp[1]) + a
    new_min[1] = min(min_dp[0], min_dp[1], min_dp[2]) + b
    new_min[2] = min(min_dp[1], min_dp[2]) + c

    max_dp = new_max
    min_dp = new_min

# 출력
print(max(max_dp), min(min_dp))