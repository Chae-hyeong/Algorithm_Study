import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lenghts = [int(input()) for _ in range(K)]

start, end = 1, max(lenghts)
answer = 0

while start <= end:
    mid = (start + end) // 2
    cnt = sum(l // mid for l in lenghts)

    if cnt >= N:
        start = mid + 1
        answer = mid

    else:
        end = mid - 1

print(answer)