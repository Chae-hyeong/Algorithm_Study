import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 2차원 누적 합 배열
prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix_sum[i][j] = (
            graph[i-1][j-1]
            + prefix_sum[i-1][j]
            + prefix_sum[i][j-1]
            - prefix_sum[i-1][j-1]
        )

# 질의 처리
K = int(input())
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    result = (
        prefix_sum[x2][y2]
        - prefix_sum[x1-1][y2]
        - prefix_sum[x2][y1-1]
        + prefix_sum[x1-1][y1-1]
    )
    print(result)