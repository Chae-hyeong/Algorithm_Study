import sys
input = sys.stdin.readline

mod = 10**9 + 7

# 입력 처리
n = int(input())
m = list(map(int, input().split()))

arr = []  # 성능 누적 배열
total_sum = 0  # 최종 결과 합

for i in range(n - 1):
    a = m[i]  # 성능 배수 입력
    if i == 0:
        arr.append(a)
        total_sum += a % mod  # 첫 번째 값 처리
    else:
        tmp = (a * arr[i - 1] + a) % mod  # 누적 계산
        arr.append(tmp)
        total_sum += tmp % mod  # 누적 합계

# 결과 출력
print(total_sum % mod)