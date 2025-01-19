import sys

input = sys.stdin.readline

N, M = map(int, input().split())
valid = True

for _ in range(M):
    int(input())
    stack = list(map(int, input().split()))

    if stack != sorted(stack, reverse=True):
        valid = False

print("Yes" if valid else "No")