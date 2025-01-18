import sys
input = sys.stdin.readline

# 입력
R, C = map(int, input().split())
N = int(input())

# 유물 정보
artifacts = {}

# 유물 정보 입력 처리
for _ in range(N):
    a, v, h = map(int, input().split())

    if a not in artifacts:
        artifacts[a] = [v, v, h, h]  # 초기값 설정 (min_row, max_row, min_col, max_col)
    else:
        # 최소/최대 행, 열 갱신
        artifacts[a][0] = min(artifacts[a][0], v)  # min_row
        artifacts[a][1] = max(artifacts[a][1], v)  # max_row
        artifacts[a][2] = min(artifacts[a][2], h)  # min_col
        artifacts[a][3] = max(artifacts[a][3], h)  # max_col

# 가장 큰 유물을 찾기
target = None
max_size = 0

for a, (min_row, max_row, min_col, max_col) in sorted(artifacts.items()):  # 번호 작은 것부터 탐색
    size = (max_row - min_row + 1) * (max_col - min_col + 1)  # 직사각형 크기 계산

    if size > max_size:
        max_size = size
        target = a

# 결과 출력
print(target, max_size)