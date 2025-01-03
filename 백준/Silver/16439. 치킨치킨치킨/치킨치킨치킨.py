import sys
from itertools import combinations

input = sys.stdin.readline

#N, M, 선호도 입력받기
N,M = map(int, input().split())
preferences = [list(map(int, input().split())) for _ in range(N)]

# 만족도 합의 최댓값
max_total = 0

# 조합
for combo in combinations(range(M), 3):
    total = 0

    for pref in preferences:
        max_pref = max(pref[combo[0]], pref[combo[1]], pref[combo[2]])
        total += max_pref

    max_total = max(max_total, total)

print(max_total)