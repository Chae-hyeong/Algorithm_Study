import sys
import math

input = sys.stdin.readline

def count_pairs(N):
    count = 0
    for d in range(1, int(math.sqrt(N)) + 1):
        if N % d == 0:
            A, B = d, N // d
            if math.gcd(A, B) == 1:
                count += 1
    return count

T = int(input().strip())

for _ in range(T):
    N = int(input())
    print(count_pairs(N))