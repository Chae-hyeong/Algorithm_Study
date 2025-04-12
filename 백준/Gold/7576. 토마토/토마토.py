import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque((i, j) for i in range(N) for j in range(M) if graph[i][j] == 1)

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

bfs()

if any(0 in row for row in graph):
    print(-1)
    sys.exit()

print(max(map(max, graph)) - 1)