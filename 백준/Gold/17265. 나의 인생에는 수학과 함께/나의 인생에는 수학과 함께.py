import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [input().split() for _ in range(n)]

dx = [1, 0]
dy = [0, 1]

def calculate(a, b, op):
    a, b = int(a), int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def bfs():
    q = deque()
    q.append((0, 0, graph[0][0], ''))

    max_val = -float('inf')
    min_val = float('inf')

    while q:
        x, y, value, op = q.popleft()

        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cell = graph[nx][ny]

                if cell in '+-*':
                    q.append((nx, ny, value, cell))
                else:
                    new_value = calculate(value, cell, op)
                    if nx == n - 1 and ny == n - 1:
                        max_val = max(max_val, new_value)
                        min_val = min(min_val, new_value)
                    else:
                        q.append((nx, ny, new_value, ''))

    return max_val, min_val

maximum, minimum = bfs()
print(maximum, minimum)