# 태권왕

import sys
from collections import deque

input = sys.stdin.readline

def bfs(S, T):
    use = [[-1] * 201 for _ in range(201)]
    q = deque()
    q.append((0, S, T))
    use[S][T] = 0

    while q:
        cnt, S, T = q.popleft()

        if S == T:
            return cnt

        # A 발차기
        ns, nt = S * 2, T + 3
        if ns <= 200 and nt <= 200 and use[ns][nt] == -1:
            use[ns][nt] = cnt + 1
            q.append((cnt + 1, ns, nt))

        # B 발차기
        ns, nt = S + 1, T
        if ns <= 200 and use[ns][nt] == -1:
            use[ns][nt] = cnt + 1
            q.append((cnt + 1, ns, nt))


C = int(input())
for _ in range(C):
    S, T = map(int, input().split())
    print(bfs(S, T))
