import sys
input = sys.stdin.readline

# 입력된 시간 (시, 분)과 추가해야 할 분을 받습니다.
current_time = list(map(int, input().split()))
additional_minutes = int(input())

# 시간을 모두 분으로 변환하여 더해줍니다.
total_minutes = current_time[0] * 60 + current_time[1] + additional_minutes

# 다시 시와 분으로 나누어 결과를 저장합니다.
current_time[0] = total_minutes // 60
current_time[1] = total_minutes % 60

if current_time[0] >= 24:
    current_time[0] = current_time[0] - 24

# 결과 출력
print(*current_time)