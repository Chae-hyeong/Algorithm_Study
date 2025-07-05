import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
graph = [list(input().split()) for _ in range(n)]
teacher = sum(row.count('T') for row in graph)

def check_S(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        while 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 'O':
            if graph[nx][ny] == 'S':
                return True
            else:
                nx += dx[i]
                ny += dy[i]
    return False

def solution(count):
  global answer
  if count == 3:
    cnt = 0
    for i in range(n):
      for j in range(n):
        if graph[i][j] == 'T':
          if not check_S(i,j):
            cnt+=1
    if cnt == teacher:
      answer = True
    return

  for i in range(n):
    for j in range(n):
      if graph[i][j] == 'X':
        graph[i][j] = 'O'
        count +=1
        solution(count)
        graph[i][j] = 'X'
        count -=1

answer = False
solution(0)
if answer:
  print('YES')
else:
  print('NO')