import sys
input = sys.stdin.readline

for _ in range(3):
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    S = sum(arr)

    if S == 0:
        print(0)
    if S > 0:
        print("+")
    if S < 0:
        print("-")