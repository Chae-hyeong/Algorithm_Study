from collections import deque

N, K = map(int, input().split())
MAX = 100001
visited = [False] * MAX

q = deque()
q.append((N, 0))

while q:
    pos, time = q.popleft()

    if pos == K:
        print(time)
        break

    for next_pos in (pos - 1, pos + 1, pos * 2):
        if 0 <= next_pos < MAX and not visited[next_pos]:
            visited[next_pos] = True
            q.append((next_pos, time + 1))
