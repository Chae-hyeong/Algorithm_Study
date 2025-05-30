import sys, heapq
INF = int(1e9)

input = sys.stdin.readline


n,m = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1) 

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

start, end = 1, n 

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(distance[end])