import sys
import math

input = sys.stdin.readline

def main():
    while True:
        n, k = map(int, input().split())

        if n == 0 and k == 0:
            break

        print(math.comb(n, k))

if __name__ == "__main__":
    main()