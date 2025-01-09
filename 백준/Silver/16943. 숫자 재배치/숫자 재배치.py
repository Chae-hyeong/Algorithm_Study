import sys
from itertools import permutations

input = sys.stdin.readline

A, B = map(int, input().split())

perm_list = list(permutations(str(A), len(str(A))))

max_num = -1

for perm in perm_list:
    C = int(''.join(perm))

    if C < B and len(str(A)) == len(str(C)):
        max_num = max(max_num, C)

print(max_num)