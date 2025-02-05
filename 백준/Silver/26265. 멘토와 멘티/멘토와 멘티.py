import sys
input = sys.stdin.readline

# 순서쌍 수
N = int(input())

# 순서쌍 딕셔너리 초기화
pairs = {}

for _ in range(N):
    # 멘토, 멘티 입력
    mentor, mentee = map(str, input().split())

    if mentor in pairs:
        pairs[mentor].append(mentee)
    else:
        pairs[mentor] = [mentee]

# 출력
# 1. 멘토 기준 사전 수
# 2. 멘티 역순
# 3. 쌍 하나씩 출력
print(*[f"{mentor} {mentee}" 
        for mentor, mentees in sorted(pairs.items())
        for mentee in sorted(mentees, reverse=True)], sep = '\n')