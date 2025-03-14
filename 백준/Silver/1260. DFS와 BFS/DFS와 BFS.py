import sys
from collections import deque

input = sys.stdin.readline

def dfs(start, graph, visited, result):
    visited[start] = True
    result.append(start)
    for c in graph[start]:
        if not visited[c]:
            dfs(c, graph, visited, result)

def bfs(start, graph, visited):
    q = deque([start])
    visited[start] = True
    result = [start]

    while q:
        current = q.popleft()
        for c in graph[current]:
            if not visited[c]:
                visited[c] = True
                q.append(c)
                result.append(c)
    return result

# 입력
N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 정렬
for i in range(1, N + 1):
    graph[i].sort()

# DFS
visited_dfs = [False] * (N + 1)
dfs_result = []
dfs(V, graph, visited_dfs, dfs_result)
print(' '.join(map(str, dfs_result)))

# BFS
visited_bfs = [False] * (N + 1)
bfs_result = bfs(V, graph, visited_bfs)
print(' '.join(map(str, bfs_result)))