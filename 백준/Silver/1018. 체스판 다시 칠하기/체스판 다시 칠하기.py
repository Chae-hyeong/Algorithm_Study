# 입력
N, M = map(int, input().split())
chess = [input() for _ in range(N)]

# 체스판 패턴
pattern1 = ["WBWBWBWB", "BWBWBWBW"] * 4
pattern2 = ["BWBWBWBW", "WBWBWBWB"] * 4

# 최소 필해야 하는 칸 수
min_repaints = float('inf')
# 선택할 수 있는 행
for row in range(N-7):
    for col in range(M-7):
        count1 = 0  # 패턴 1
        count2 = 0  # 패턴 2

        for i in range(8):
            for j in range(8):
                color = chess[row+i][col+j]

                if color != pattern1[i][j]:
                    count1 += 1

                if color != pattern2[i][j]:
                    count2 += 1

        min_repaints = min(min_repaints, count1, count2)

print(min_repaints)