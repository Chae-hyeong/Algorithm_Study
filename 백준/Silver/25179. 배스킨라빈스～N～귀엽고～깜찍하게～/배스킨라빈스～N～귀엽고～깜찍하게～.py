# 입력 처리
N, M = map(int, input().split())

# 결과 출력 
print("Can't win") if N % (M + 1) == 1 else print("Can win")