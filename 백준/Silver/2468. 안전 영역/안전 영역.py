from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy, visited):
    q = deque([(sx, sy)])
    visited[sx][sy] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
max_depth = max(map(max, graph))

result = 0
for h in range(max_depth + 1):
    visited = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if graph[x][y] <= h:
                visited[x][y] = 1

    safe_cnt = 0
    for x in range(n):
        for y in range(n):
            if visited[x][y] == 0:
                bfs(x, y, visited)
                safe_cnt += 1
    result = max(result, safe_cnt)

print(result)