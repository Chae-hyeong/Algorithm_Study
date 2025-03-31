import sys
input = sys.stdin.readline

N = int(input())
visited = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x1, y1 = map(int, input().split())
    for x in range(x1, x1+10):
        for y in range(y1, y1+10):
            visited[x][y] = 1

result = 0
for i in range(100):
    result += visited[i].count(1)

print(result)