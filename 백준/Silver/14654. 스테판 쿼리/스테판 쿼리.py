import sys
input = sys.stdin.readline

# 입력
n = int(input())
team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))

# 초기화
cnt1, cnt2, ans = 0, 0, 0

# 라운드 진행
for i in range(n):
    if (team1[i] == 1 and team2[i] == 2) or \
       (team1[i] == 2 and team2[i] == 3) or \
       (team1[i] == 3 and team2[i] == 1):  # teamB 승리
        cnt1 = 0
        cnt2 += 1
    elif (team2[i] == 1 and team1[i] == 2) or \
         (team2[i] == 2 and team1[i] == 3) or \
         (team2[i] == 3 and team1[i] == 1):  # teamA 승리
        cnt2 = 0
        cnt1 += 1
    else:  # 비긴 경우
        if cnt1 > 0:
            cnt1 = 0
            cnt2 += 1
        else:
            cnt2 = 0
            cnt1 += 1

    # 연승 갱신
    ans = max(ans, cnt1, cnt2)

# 출력
print(ans)