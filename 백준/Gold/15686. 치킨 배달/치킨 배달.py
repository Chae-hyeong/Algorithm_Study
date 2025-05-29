import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

homes = []
chickens = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            homes.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

def get_chicken_distance(chicken_comb):
    total = 0
    for hx, hy in homes:
        dist = 1e9
        for cx, cy in chicken_comb:
            dist = min(dist, abs(hx - cx) + abs(hy - cy))
        total += dist
    return total

result = 1e9
for comb in combinations(chickens, m):
    result = min(result, get_chicken_distance(comb))

print(result)