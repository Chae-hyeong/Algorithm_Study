import sys
input = sys.stdin.readline

# 입력
n = int(input())
num = [0] + list(map(int, input().split()))
k = int(input())

# (0,0) 외에 교점 확인
for i in range(1, n+1):
    if num[i] == k * i:
        print("T")
        exit()

    # 구간 내에서 y = kx가 지나가는 경우
    if (num[i-1] - k * (i-1)) * (num[i] - k * i) < 0:
        print("T")
        exit()

# 모든 경우에서 교점이 없는 경우
print("F")