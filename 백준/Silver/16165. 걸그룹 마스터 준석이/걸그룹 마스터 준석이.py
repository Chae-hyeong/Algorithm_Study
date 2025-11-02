import sys
input = sys.stdin.readline

group_total, quiz_total = map(int, input().split())

groups = {}
members = {}

for i in range(group_total):
    group_name = input().strip()
    member_total = int(input())
    group_member = [None] * member_total
    for i in range(member_total):
        member = input().strip()
        group_member[i] = member
        members[member] = group_name
    group_member.sort()
    groups[group_name] = (
        tuple(group_member)
    )
    
def solve_quiz(quiz, quiz_type):
    if quiz_type == 1:
        find_group = members[quiz]
        print(find_group)
    elif quiz_type == 0:
        group = groups[quiz]
        for member in group:
            print(member)

for i in range(quiz_total):
    quiz = input().strip()
    quiz_type = int(input())
    solve_quiz(quiz, quiz_type)