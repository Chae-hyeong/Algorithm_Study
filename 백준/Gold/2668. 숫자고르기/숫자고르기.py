
import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
graph = defaultdict(list)

for i in range(1, n + 1):
    graph[i].append(arr[i - 1])

result = []

def dfs(current, start, visited):
    visited[current] = True
    next_node = graph[current][0]

    if not visited[next_node]:
        dfs(next_node, start, visited)
    elif next_node == start:
        result.append(start)

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dfs(i, i, visited)

result.sort()
print(len(result))
for num in result:
    print(num)