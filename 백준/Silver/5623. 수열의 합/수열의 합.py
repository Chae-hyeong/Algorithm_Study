import sys
input = sys.stdin.readline

# 입력
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

if N == 2: 
    print("1 1")
else:
    # 첫 번째 값(one) 계산
    one = (graph[0][1] + graph[0][2] - graph[1][2]) // 2

    # 결과 저장 리스트
    ans = [0] * N
    ans[0] = one

    # 나머지 값 계산
    for i in range(1, N):
        ans[i] = graph[0][i] - one

    # 출력
    print(*ans)