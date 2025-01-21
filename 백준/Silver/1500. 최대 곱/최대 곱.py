import math

# 입력 받기
S, K = map(int, input().split())

# 몫과 나머지 계산
q, r = divmod(S, K)

# 최대 곱 계산 (r개는 q+1, 나머지는 q)
max_product = (math.prod([q + 1] * r) * math.prod([q] * (K - r)))

# 출력
print(max_product)