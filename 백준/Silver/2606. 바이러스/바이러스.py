import sys
from collections import deque

def bfs(start, graph, visited):
    queue = deque([start])
    visited[start] = 1

    while queue:
        current = queue.popleft()
        for c in graph[current]:
            if visited[c] == 0:
                visited[c] = 1
                queue.append(c)

def main():
    input = sys.stdin.readline

    n = int(input())
    v = int(input())
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)

    for _ in range(v):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    bfs(1, graph, visited)
    print(sum(visited) - 1)

if __name__ == '__main__':
    main()
