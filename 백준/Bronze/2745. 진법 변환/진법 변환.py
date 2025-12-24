n, b = input().split()
n = "".join(reversed(n))
b = int(b)
nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = 0

for i in range(len(n) - 1, -1, -1):
    result += (nums.index(n[i])) * (int(b) ** i)

print(result)