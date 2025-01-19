import sys

input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
valid = True # 정렬 여부

for _ in range(M):
    int(input()) # 더미 크기 필요 없음
    stack = list(map(int, input().split()))

    if stack != sorted(stack, reverse=True): # 내림차순 정렬이 아닌 경우
        valid = False

print("Yes" if valid else "No")
