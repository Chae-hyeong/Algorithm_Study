import sys
input = sys.stdin.readline

# 입력
X = int(input())  # 전체 참가자 수
N = int(input())  # 스태프 수

minimum_votes = X * 0.05  
staff_votes = {} 

# 유효한 스태프 저장
for _ in range(N):
    name, votes = input().split()
    votes = int(votes)

    if votes >= minimum_votes:
        staff_votes[name] = votes  # 후보 스태프 저장

# 2. 각 스태프의 점수 계산
scores = []
for name, votes in staff_votes.items():
    for i in range(1, 15):
        scores.append((votes / i, name))

# 3. 점수 내림차순 정렬 (높은 순서대로 정렬)
scores.sort(reverse=True, key=lambda x: x[0])

# 4. 상위 14개 점수에 대해 해당 스태프에게 칩 부여
staff_chips = {name: 0 for name in staff_votes}
for i in range(14):  
    _, staff_name = scores[i]
    staff_chips[staff_name] += 1

# 5. 사전순 정렬 후 출력
for name in sorted(staff_chips):
    print(name, staff_chips[name])