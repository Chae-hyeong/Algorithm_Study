import sys

if __name__ == '__main__':
    k = int(sys.stdin.readline().rstrip())
    a, b, c, d = map(int, sys.stdin.readline().rstrip().split())
    if a*k+b == c*k+d:
        print('Yes', a*k+b)
    else:
        print('No')