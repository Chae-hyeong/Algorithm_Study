import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * n
answer = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(idx, cnt):
    global answer
    if answer:
        return
    if cnt == 4:
        answer = 1
        return

    visited[idx] = True
    for i in graph[idx]:
        if not visited[i]:
            dfs(i, cnt + 1)
    visited[idx] = False

for i in range(n):
    dfs(i, 0)
    if answer:
        break

print(1 if answer else 0)