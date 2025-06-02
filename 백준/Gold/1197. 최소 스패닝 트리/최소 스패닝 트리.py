import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

v, e = map(int, input().split())
parent = [i for i in range(v + 1)]

edges = sorted([(cost, a, b) for a, b, cost in [map(int, input().split()) for _ in range(e)]])
result = 0

def fine_parent(parent, x):
    if parent[x] != x:
        parent[x] = fine_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = fine_parent(parent, a)
    b = fine_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for edge in edges:
    cost, a, b = edge
    if fine_parent(parent, a) != fine_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)