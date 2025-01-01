# 입력 받기
a2, a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

# 조건에 따른 처리
if c == a2:  # 최고차항 계수가 동일한 경우 (직선)
    result = (a1 <= 0 and ((c - a2) * n0 * n0 - (a1 * n0) - a0) >= 0)
elif a2 > c:  # 최고차항이 더 크면 위로 볼록한 2차 함수
    result = False
else:  # 아래로 볼록한 2차 함수
    if a1 > 2 * (c - a2) * n0:  # 축이 n0 왼쪽에 있는 경우
        result = (a1 * a1 + 4 * a0 * (c - a2) <= 0)
    else:  # n0에서의 값을 확인
        result = ((c - a2) * n0 * n0 - (a1 * n0) - a0 >= 0)

# 결과 출력
print(1 if result else 0)