import sys
input = sys.stdin.readline

# 배열 및 메모이제이션 초기화
d = [[-1] * 303 for _ in range(303)]
arr = [[False] * 303 for _ in range(303)]

# 입력 처리
n, m = map(int, input().split())
for _ in range(n):
    x, y = map(int, input().split())
    arr[x][y] = True

# DP 진행
for x in range(300, -1, -1):
    for y in range(300, -1, -1):
        cnt = max(0, m - x - y) if arr[x][y] else 0
        from_right = d[x+1][y] if x < 300 else 0
        from_down = d[x][y+1] if y < 300 else 0
        d[x][y] = max(from_right, from_down) + cnt

# 결과 출력
print(d[0][0])