
# 입력
X = int(input())

# DP 테이블 초기화
dp = [0] * (X + 1)

# 2부터 N까지 최소 연산 횟수 계산
for i in range(2, X + 1):
    # 1을 빼는 경우
    dp[i] = dp[i - 1] + 1

    # 2로 나눌 수 있는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # 3으로 나눌 수 있는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

# 출력
print(dp[X])