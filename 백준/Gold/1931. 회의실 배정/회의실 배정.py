import sys
input = sys.stdin.readline

N = int(input())
info = [tuple(map(int, input().split())) for _ in range(N)]

info.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for start, end in info:
    if start >= end_time:
        count += 1
        end_time = end

print(count)