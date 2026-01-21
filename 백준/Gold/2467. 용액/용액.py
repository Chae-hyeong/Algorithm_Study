n = int(input())
arr = list(map(int, input().split()))

start, end = 0, n - 1
current_sum = 0
min_sum = float('inf')
acid, alkaline = 0, 0

while start < end:
    current_sum = arr[start] + arr[end]
    if abs(current_sum) < abs(min_sum):
        min_sum = current_sum
        acid = arr[start]
        alkaline = arr[end]
    if current_sum > 0:
        end -= 1
    elif current_sum < 0:
        start += 1
    else:
        break

print(acid, alkaline)