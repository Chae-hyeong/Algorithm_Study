from itertools import product

# 입력
N = int(input())

# 중복 순열
nums = [int("".join(map(str, d))) for d in product(range(3), repeat = N) if d[0] != 0]

# 3의 배수
cnt = sum(1 for num in nums if num % 3 == 0)

# 출력
print(cnt)