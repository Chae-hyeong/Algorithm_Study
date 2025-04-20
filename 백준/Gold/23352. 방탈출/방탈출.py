import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy):
    visited = [[-1] * M for _ in range(N)]
    visited[sx][sy] = 0
    queue = deque([(sx, sy)])
    result = []

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                    result.append((visited[nx][ny], graph[sx][sy] + graph[nx][ny]))

    return result

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

max_d, max_s = 0, 0

for i in range(N):
    for j in range(M):
        if graph[i][j]:
            for d, s in bfs(i, j):
                if d > max_d:
                    max_d, max_s = d, s
                elif d == max_d:
                    max_s = max(max_s, s)

print(max_s if max_d else 0)