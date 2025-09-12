input = __import__('sys').stdin.readline

m,n = map(int,input().split())
x=0
y=0
dx = [1,0,-1,0]
dy = [0,-1,0,1]
state = 0
flag = True
for i in range(n):
    a,b = map(str, input().split())
    if a == "MOVE":
        x += int(b) * dx[state]
        y += int(b) * dy[state]
    else:
        if int(b) == 1:
            state = (state+1)%4
        else:
            state -= 1
            if state < 0:
                state = 3

    if x < 0 or y < 0 or x >= m or y >= m:
        flag = False

if flag == False:
    print(-1)
else:
    print(x,y)