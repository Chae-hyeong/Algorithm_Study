# 입력 처리
N = int(input())
max_bishop = 2 * N - 2

if N == 1:
    print(1)
    print("1 1")
else:
    # 최대 비콘 수 출력
    print(max_bishop)
    
    # 첫 행과 마지막 행의 비숍 배치
    for i in range(1,N+1):
        print(f"1 {i}")
        if i != 1 and i != N:
            print(f"{N} {i}")