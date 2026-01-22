import sys
input = sys.stdin.readline

n = int(input())

start = 0
cnt = 0
current_sum = 0

for end in range(n+1):
    current_sum += end

    while current_sum > n and start <= end:
        current_sum -= start
        start += 1

    if current_sum == n:
        cnt += 1

print(cnt)