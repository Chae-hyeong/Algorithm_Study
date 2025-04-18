import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    homes[x][y] = 0
    count = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and homes[nx][ny] == 1:
                homes[nx][ny] = 0
                queue.append((nx, ny))
                count += 1

    return count

n = int(input())
homes = [list(map(int, input().strip())) for _ in range(n)]

result = []

for i in range(n):
    for j in range(n):
        if homes[i][j] == 1:
            result.append(bfs(i, j))

result.sort()
print(len(result))
print(*result, sep='\n')