import sys, heapq
from collections import deque

input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
Rs = [int(input()) for _ in range(N)]
Wk = [int(input()) for _ in range(M)]
events = [int(input()) for _ in range(2 * M)]

# 초기화
empty_spaces = list(range(N))  
heapq.heapify(empty_spaces)    
waiting_queue = deque()        
parking_status = {}            

total_income = 0

for event in events:
    if event > 0:  # 차량이 들어올 때
        car_id = event - 1  

        if empty_spaces:  # 빈 주차 공간이 있으면
            space_id = heapq.heappop(empty_spaces)
            parking_status[car_id] = space_id
            total_income += Wk[car_id] * Rs[space_id]
        else:
            waiting_queue.append(car_id)  # 빈 공간이 없으면 대기열에 추가

    else:  # 차량이 나갈 때
        car_id = -event - 1
        space_id = parking_status.pop(car_id)  # 차량이 차지한 공간 확인
        heapq.heappush(empty_spaces, space_id)  # 주차 공간을 빈 공간으로 복구

        if waiting_queue:  # 대기 중인 차량이 있으면 바로 주차
            next_car_id = waiting_queue.popleft()
            space_id = heapq.heappop(empty_spaces)
            parking_status[next_car_id] = space_id
            total_income += Wk[next_car_id] * Rs[space_id]

# 출력
print(total_income)