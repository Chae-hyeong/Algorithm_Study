import sys
input = sys.stdin.readline

T = int(input())
answer = ''

for _ in range(T):
    s = input().strip()
    answer = s[0] + s[-1]
    print(answer)