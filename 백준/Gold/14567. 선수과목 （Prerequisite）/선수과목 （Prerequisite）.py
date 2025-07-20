import sys
from collections import deque

def initialize_variables():
    v, e = map(int, sys.stdin.readline().split())
    indegrees = [0] * (v+1)
    edges = [[] for _ in range(v+1)]
    for _ in range(e):
        src, dest = map(int, sys.stdin.readline().split())
        indegrees[dest] += 1
        edges[src].append(dest)
    return v, e, indegrees, edges

def initialize_queue():
    queue = deque([])
    for i in range(1, v+1):
        if indegrees[i] == 0:
            queue.append((1, i))
    return queue

def solve(v, e, indegrees, edges, queue):
    result = [1] * (v+1)
    while queue:
        depth, node = queue.popleft()
        result[node] = max(result[node], depth)
        for next_node in edges[node]:
            indegrees[next_node] -= 1
            if indegrees[next_node] == 0:
                queue.append((depth+1, next_node))
    return result[1:]

v, e, indegrees, edges = initialize_variables()
queue = initialize_queue()
answer = solve(v, e, indegrees, edges, queue)
print(' '.join(map(str, answer)))