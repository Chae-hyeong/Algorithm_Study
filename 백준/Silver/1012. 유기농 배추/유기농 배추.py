import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]
    cnt = 0

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for a in range(M):
        for b in range(N):
            if graph[a][b] == 1:
                bfs(a, b)
                cnt += 1

    print(cnt)