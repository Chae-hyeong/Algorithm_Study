import math

M, N = map(int, input().split())

arr = [True for _ in range(N + 1)]
arr[0], arr[1] = False, False  # 0과 1은 소수가 아님

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(N)) + 1):
    if arr[i]:
        for j in range(i * i, N + 1, i):  # i*i부터 시작
            arr[j] = False

# M부터 N까지 소수 출력
for i in range(M, N + 1):
    if arr[i]:
        print(i)