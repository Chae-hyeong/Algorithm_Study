import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0] = 1

    while q:
        x, y, has_sword = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny][has_sword] == 0:
                    cell = graph[nx][ny]

                    if cell == 0:
                        visited[nx][ny][has_sword] = visited[x][y][has_sword] + 1
                        q.append((nx, ny, has_sword))

                    elif cell == 2:
                        visited[nx][ny][1] = visited[x][y][has_sword] + 1
                        q.append((nx, ny, 1))

                    elif cell == 1 and has_sword == 1:
                        visited[nx][ny][has_sword] = visited[x][y][has_sword] + 1
                        q.append((nx, ny, has_sword))

    return visited

N, M, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

visited = bfs()

without_sword = visited[N-1][M-1][0]
with_sword = visited[N-1][M-1][1]

min_time = float('inf')
if without_sword:
    min_time = without_sword - 1
if with_sword:
    min_time = min(min_time, with_sword - 1)

if min_time <= T:
    print(min_time)
else:
    print("Fail")
