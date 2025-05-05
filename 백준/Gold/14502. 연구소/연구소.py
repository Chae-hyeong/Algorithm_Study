import sys
from collections import deque

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    global answer
    tmp = [row[:] for row in graph]
    q = deque()

    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                q.append((nx, ny))

    safe = sum(row.count(0) for row in tmp)
    answer = max(answer, safe)

def makeWall(start, cnt):
    if cnt == 3:
        bfs()
        return

    for idx in range(start, len(zero)):
        x, y = zero[idx]
        graph[x][y] = 1
        makeWall(idx + 1, cnt + 1)
        graph[x][y] = 0

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
zero = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]

answer = 0
makeWall(0, 0)
print(answer)