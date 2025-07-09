import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
times = sorted(list(map(int, input().split())), reverse=True)
heap = []

for t in times:
    if len(heap) < m:
        heapq.heappush(heap, t)
    else:
        heapq.heapreplace(heap, heap[0] + t)

print(max(heap))