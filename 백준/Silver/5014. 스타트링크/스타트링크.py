from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F + 1)]

def bfs():
    queue = deque()
    queue.append(S)

    visited[S] = 1

    while queue:
        q = queue.popleft()
        if q == G:
            return visited[q] - 1

        for x in (q + U, q - D):
            if (1 <= x <= F) and visited[x] == 0:
                queue.append(x)
                visited[x] = visited[q] + 1


result = bfs()
print(result if result != None else "use the stairs")
