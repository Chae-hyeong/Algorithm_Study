import math

def get_count(a, b):
    result = 0
    i = 0
    cur = (2 ** i) - 1

    while cur <= a + b:
        if cur <= a and cur <= b:
            result += cur + 1
        elif cur <= a and cur > b:
            result += b + 1
        elif cur <= b and cur > a:
            result += a + 1
        else:
            result += a + b - cur + 1
        i += 1
        cur = (2 ** i) - 1

    return result


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(get_count(a, b))

