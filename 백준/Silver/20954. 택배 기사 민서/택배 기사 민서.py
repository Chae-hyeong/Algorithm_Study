
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x = int(input())
    expo = 0

    while 2**expo < abs(x):
        expo += 1

    if x == 0:
        print(0)
    elif x > 0:
        print(5 * 2**expo - 4 - (2**expo - x))
    else:
        print(5 * 2**expo - 4 + 2**(expo+1) - (2**expo - abs(x)))