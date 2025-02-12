import sys
import math

input = sys.stdin.readline

def find_position(n, k):
    n -= 1
    if n < k:
        return n, 'R'

    m = int((-1 + math.sqrt(1 + (8 * n / k))) // 2)
    length = k * (m * (m + 1) // 2)
    left_length = n - length
    pos = ((m - 1) // 2 + 1) * k * (1 if m % 2 == 1 else -1)

    if m % 2 == 1:
        return pos - left_length, 'L'
    else:
        return pos + left_length, 'R'


T = int(input().strip())
results = []

for _ in range(T):
    N, K = map(int, input().split())
    results.append(f"{find_position(N, K)[0]} {find_position(N, K)[1]}")

sys.stdout.write('\n'.join(results) + '\n')