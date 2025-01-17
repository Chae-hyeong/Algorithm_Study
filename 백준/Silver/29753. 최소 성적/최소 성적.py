import sys
import math

input = sys.stdin.readline

# 성적 변환 테이블
grade_dict = {"F": 0.00, "D0": 1.00, "D+": 1.50, "C0": 2.00, "C+": 2.50, "B0": 3.00, "B+": 3.50, "A0": 4.00, "A+": 4.50}

# 수강 과목 수, 최소 평균 평점 기준
N, X = input().split()
N, X = int(N), float(X)

# 학점 성적
courses = [(int(c), g) for _ in range(N - 1) for c, g in [input().split()]]

# 나머지 학점
L = int(input())

# 현재까지의 학점 * 점수 합 및 총 학점 계산
sum_score = sum(c * grade_dict[g] for c, g in courses) # 학점 * 점수
total_credits = sum(c for c, _ in courses) + L # 총 학점

answer = "impossible"

# 가능한 최소 성적 찾기 (F부터 A+까지)
for key, value in grade_dict.items():
    total_score = sum_score + (L * value)
    total_gpa = '%.3f'%(total_score / total_credits)

    if float(total_gpa[:4]) > X:
        answer = key
        break

print(answer)
