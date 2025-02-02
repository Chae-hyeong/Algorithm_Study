
import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 누적 합 배열 생성
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

# 쿼리 처리
for _ in range(M):
    start, end = map(int, input().split())
    result = prefix_sum[end] - prefix_sum[start - 1]
    print(result)