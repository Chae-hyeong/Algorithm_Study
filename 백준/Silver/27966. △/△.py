# 정점의 개수
N = int(input())

# 두 정점 사이 거리의 합의 최소
min_distance = (N - 1) + (N - 2) * (N - 1)

# 출력
print(min_distance)
for node in range(2, N + 1):
    print(1, node)