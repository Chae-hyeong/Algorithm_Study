import sys
input = sys.stdin.readline

# 입력
N = int(input())
A = list(map(int, input().split()))

# 등장 횟수 카운트 및 초기 XOR 합 계산
xor_sum = 0
for num in A:
    xor_sum ^= num

# 숫자 제거 -> 최댓값 갱신
best_sum = xor_sum
for num in A:
    new_sum = xor_sum ^ num  # num을 제거한 XOR 값 계산
    best_sum = max(best_sum, new_sum)

# 출력
print(f"{best_sum}"*2)