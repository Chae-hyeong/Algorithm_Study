from collections import deque

# 입력
N = int(input())
cards = deque(i for i in range(1, N+1))

while len(cards) > 1:
    del cards[0] # 제일 위 카드 버리기
    cards.append(cards.popleft())  # 다음 카드를 아래로 이동

# 출력
print(cards[0])