import sys
import math

input = sys.stdin.readline

# 케이스 수
T = int(input())

for _ in range(T):
    # 입력
    A, B, X = map(int, input().split())

    # 개구리는 도달할 수 있는 위치는 GCD(A, B)의 배수 
    answer = X // math.gcd(A, B)

    print(answer)