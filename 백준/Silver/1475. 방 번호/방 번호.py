n = input()
arr = [0] * 10

for i in range(len(n)):
    if n[i] == '9' or n[i] == '6':
        arr[6] += 1
    else:
        arr[int(n[i])] += 1

arr[6] = (arr[6] + 1) // 2

print(max(arr))