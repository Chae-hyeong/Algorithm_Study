import sys
from collections import deque

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
t = min(n, m) // 2
answer = [[0] * m for _ in range(n)]
q = deque()

for i in range(t):
    q.clear()
    q.extend(graph[i][i:m-i])
    q.extend(graph[j][m-i-1] for j in range(i+1, n-i-1))
    q.extend(graph[n-i-1][i:m-i][::-1])
    q.extend(graph[j][i] for j in range(n-i-2, i, -1))

    q.rotate(-r)

    for j in range(i, m-i):
        answer[i][j] = q.popleft()
    for j in range(i+1, n-i-1):
        answer[j][m-i-1] = q.popleft()
    for j in range(m-i-1, i-1, -1):
        answer[n-i-1][j] = q.popleft()
    for j in range(n-i-2, i, -1):
        answer[j][i] = q.popleft()

sys.stdout.write('\n'.join(' '.join(map(str, row)) for row in answer) + '\n')