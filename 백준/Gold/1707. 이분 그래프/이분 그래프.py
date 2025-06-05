import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, group):
    q = deque(([start]))
    visited[start] = group

    while q:
        node = q.popleft()

        for link_node in graph[node]:
            if not visited[link_node]:
                q.append(link_node)
                visited[link_node] = -visited[node]
            elif visited[link_node] == visited[node]:
                return True

    return False

n = int(input())

for _ in range(n):
    v, e = map(int, input().split())

    graph = [[] for _ in range(v + 1)]
    visited = [False for _ in range(v + 1)]
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, v + 1):
        if not visited[i]:
            result = bfs(i, 1)
            if result:
                print("NO")
                break
    else:
        print("YES")

