import sys
import math

input = sys.stdin.readline

INF = 10**4

def taxes():

    total_sum = sum(prices)  # 물건의 총합
    answers = []

    # 부가세 F를 탐색
    for F in range(0, INF + 1):
        tax = total_sum * F / 100  # 부가세 계산
        # 올림, 내림한 부가세를 각각 계산
        lower_tax = math.floor(tax * 100) / 100
        upper_tax = math.ceil(tax * 100) / 100

        # 각각의 부가세를 더해 최종 결제금액 계산
        lower_total = total_sum + lower_tax
        upper_total = total_sum + upper_tax

        # 결제 금액의 달러 단위와 X 비교
        if int(lower_total) == X or int(upper_total) == X:
            answers.append(F)

    return answers

# 입력 처리
T = int(input())

for _ in range(T):
    N, X = map(int, input().split())
    prices = [float(input()) for _ in range(N)]

    # 결과
    result = taxes()
    print(min(result), max(result))
