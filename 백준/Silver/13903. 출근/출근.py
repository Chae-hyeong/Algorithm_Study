import sys
from collections import deque

input = sys.stdin.readline

# 입력 처리
R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
N = int(input())
moves = [tuple(map(int, input().split())) for _ in range(N)]

queue = deque()
visited = [[False] * C for _ in range(R)]

# 첫 번째 행의 모든 '1'을 시작점으로 추가
for col in range(C):
    if graph[0][col] == 1:
        queue.append((0, col, 0))  # 행, 열, 걸음 수
        visited[0][col] = True

# BFS 탐색
while queue:
    x, y, step = queue.popleft()

    # 마지막 행에 도달한 경우 최소 걸음 출력
    if x == R - 1:
        print(step)
        sys.exit(0)  # 프로그램 종료

    # 이동 규칙 적용
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx, ny, step + 1))

# 마지막 행에 도달하지 못한 경우
print(-1)