import sys
input=sys.stdin.readline

N,X=map(int,input().split())
data=list(map(int,input().split()))

if max(data) == 0:
    print("SAD")
else:
    value = sum(data[:X])
    
    max_value=value
    max_cnt=1

    for i in range(X,N):
        value+=data[i]
        value-=data[i-X]

        if value > max_value:
            max_value=value
            max_cnt=1
   
        elif value == max_value:
            max_cnt+=1
    print(max_value)
    print(max_cnt)