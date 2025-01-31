
N = int(input())

answer = -1
for i in range(N // 5, -1, -1):
    remainder = N - (i * 5)
    if remainder % 3 == 0:
        answer = i + (remainder // 3)
        break
print(answer)