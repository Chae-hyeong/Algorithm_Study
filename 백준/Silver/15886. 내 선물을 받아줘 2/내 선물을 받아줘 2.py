import sys
input = sys.stdin.readline

N = int(input())
maps = input()
cnt = 0

for i in range(N):
    if maps[i] == 'E' and maps[i+1] == 'W':
        cnt += 1
print(cnt)
