import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

temp = [arr[0]]
for i in range(1, n):
    temp.append(temp[i-1]+arr[i])

ans = 0
for i in range(n-1):
    ans += arr[i] * (temp[n-1]-temp[i])

print(ans)