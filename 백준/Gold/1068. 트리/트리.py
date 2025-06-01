from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

n = int(input())
nodes = list(map(int, input().split()))
delete_node = int(input())

graph = defaultdict(list)
for i in range(n):
    if nodes[i] != -1:
        graph[nodes[i]].append(i)
    else:
        root = i

deleted = set()

def mark_deleted(node):
    deleted.add(node)
    for child in graph[node]:
        mark_deleted(child)

mark_deleted(delete_node)

def count_leaves(node):
    children = [c for c in graph[node] if c not in deleted]
    if not children:
        return 1
    return sum(count_leaves(c) for c in children)

print(0 if root in deleted else count_leaves(root))