import re
import sys

input = sys.stdin.readline

t = int(input())
c = re.compile('(100+1+|01)+')
for i in range(t):
    a = c.fullmatch(input().rstrip())
    if a == None:
        print("NO")
    else:
        print("YES")