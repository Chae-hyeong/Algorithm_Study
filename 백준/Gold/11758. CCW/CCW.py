def CCW(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

P = [tuple(map(int, input().split())) for _ in range(3)]

x1, y1 = P[1][0], P[1][1]
x2, y2 = P[2][0], P[2][1]
x3, y3 = P[0][0], P[0][1]

result = CCW(x1, y1, x2, y2, x3, y3)

if result < 0:
    print(-1)
elif result > 0:
    print(1)
else:
    print(0)