import sys
from collections import deque

input = sys.stdin.readline

def bfs(a, b):
    visited = [False for _ in range(n + 1)]
    q = deque()
    q.append((a, 0))
    visited[a] = True

    while q:
        x, cnt = q.popleft()

        if x == b:
            return cnt

        for y, cost in graph[x]:
            if visited[y] == False:
                visited[y] = True
                new_dist = cnt + cost
                q.append((y, new_dist))


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    v, e, cost = map(int, input().split())
    graph[v].append((e, cost))
    graph[e].append((v, cost))

for _ in range(m):
    a, b = map(int, input().split())
    print(bfs(a, b))
