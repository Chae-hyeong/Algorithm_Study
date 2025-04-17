def generate_decreasing(num, last_digit):
    result.append(num)
    for i in range(last_digit):
        generate_decreasing(num * 10 + i, i)

n = int(input())
result = []

for i in range(10):
    generate_decreasing(i, i)

result.sort()

if n >= len(result):
    print(-1)
else:
    print(result[n])