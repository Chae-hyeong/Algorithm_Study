import sys
input = sys.stdin.readline

fibonacci = [1, 2]

while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break

    while fibonacci[-1] < b:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

    cnt = sum(1 for f in fibonacci if a <= f <= b)

    print(cnt)