# 입력
N = int(input())
beads = sorted(list(map(int, input().split())))

total = 0
for i in range(N-1):
    difference = abs(beads[i] - beads[i+1])
    total += difference

total += abs(beads[0] - beads[-1])

# 최소 길이 출력
print(total)