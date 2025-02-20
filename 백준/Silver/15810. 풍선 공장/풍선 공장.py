
import sys
input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
times = list(map(int, input().split()))

# 이분 탐색
start, end = 1, max(times) * M
result = end

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for time in times:
        cnt += mid//time

    if cnt < M:
        start = mid + 1
    else:
        result = mid
        end = mid - 1
        
# 출력
print(result)

    
