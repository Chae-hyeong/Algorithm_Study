import sys
input = sys.stdin.readline

X = int(input())
N = int(input())
cnt = sum([a * b for _ in range(N) for a, b in [map(int, input().split())]])

print("Yes" if X == cnt else "No")