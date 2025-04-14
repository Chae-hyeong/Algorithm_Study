import sys
input = sys.stdin.readline

n = int(input())
graph = [tuple(map(int, input().split())) for _ in range(n)]
graph.sort()

s, e = graph[0]
ans = 0

for i in range(1, n):
    if graph[i][0] > e:
        ans += e - s
        s, e = graph[i]
    else:
        e = max(e, graph[i][1])

ans += e - s
print(ans)