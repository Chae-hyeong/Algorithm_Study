n, k = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, k
current_sum = sum(arr[start:end])
max_sum = current_sum

while end <= n:
    start += 1
    end += 1
    if end > n:
        break
    current_sum = current_sum + arr[end-1] - arr[start-1]
    max_sum = max(max_sum, current_sum)

print(max_sum)