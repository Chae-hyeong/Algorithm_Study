n = int(input())
arr = sorted(list(map(int, input().split())))

start, end = 0, n-1
x, y = 0,0
min_sum = float('inf')

while start < end:
    current_sum = arr[start] + arr[end]
    
    #최솟값 갱신
    if abs(current_sum) < abs(min_sum):
        min_sum = current_sum
        x, y = arr[start], arr[end]

    if current_sum < 0:
        start += 1 # 합이 음수 -> 더 큰 값 필요
    elif current_sum > 0:
        end -= 1 # 합이 얍수 -> 더 작은 값 필요
    else:
        break # 합이 0

print(x, y)