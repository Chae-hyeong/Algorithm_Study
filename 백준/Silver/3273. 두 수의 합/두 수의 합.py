n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

start, end = 0, n - 1
cnt = 0

while start < end:
    sum = arr[start] + arr[end]

    if sum == x:
        cnt += 1
        start += 1
        end -= 1
    elif sum < x:
        start += 1
    else:
        end -= 1

print(cnt)