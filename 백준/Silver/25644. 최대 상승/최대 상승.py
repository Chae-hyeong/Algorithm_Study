
import sys
input = sys.stdin.readline

def two_point(N, a):
    start, end = 0, 0
    max_gain = 0

    while end < N:
        # 현재 구간의 차이 계산
        gain = a[end] - a[start]
        max_gain = max(max_gain, gain)

        # `end`를 먼저 증가시키며 구간 확장
        if a[end] >= a[start]:
            end += 1
        else:
            # `start`를 `end`로 이동해 새로운 구간 시작
            start = end

    return max_gain

# 입력 처리
N = int(input())
a = list(map(int, input().split()))

# 함수 호출 및 출력
print(two_point(N, a))