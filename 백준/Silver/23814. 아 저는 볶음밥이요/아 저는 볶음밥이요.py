
import sys
input = sys.stdin.readline

D = int(input())
N, M, K = map(int, input().split())

N = (D - (N % D)) % D
M = (D - (M % D)) % D

P = [
    (K // D, K),
    ((K - N) // D + 1, K - N),
    ((K - M) // D + 1, K - M),
    ((K - N - M) // D + 2, K - N - M)
]

P.sort()

while P and P[-1][1] < 0:
    P.pop()

print(P[-1][1])