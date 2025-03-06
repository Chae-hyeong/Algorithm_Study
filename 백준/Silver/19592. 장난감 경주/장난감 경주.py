import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, X, Y = map(int, input().split())
    V = list(map(int, input().split()))

    my_speed = V[-1]
    fastest_time = min(X / v for v in V[:-1])
    no_booster_time = X / my_speed

    if no_booster_time < fastest_time:
        print(0)
        continue
    if fastest_time <= 1.0:
        print(-1)
        continue

    def race_time(Z):
        return 1 if Z >= X else 1 + (X - Z) / my_speed

    if race_time(Y) >= fastest_time:
        print(-1)
        continue

    left, right, answer = 1, Y, Y
    while left <= right:
        mid = (left + right) // 2
        if race_time(mid) < fastest_time:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)