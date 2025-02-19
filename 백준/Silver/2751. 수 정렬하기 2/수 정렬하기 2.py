import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(int(input()) for _ in range(N)))

print(*arr, sep='\n')