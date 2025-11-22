a,b,c,d,e,f = map(int, input().split())

x,y = 0,0
for i in range(-999,1000):
    if (a*e-b*d)*i - a*f + d*c == 0:
        y = i
        break

for i in range(-999,1000):
    if d*i + e*y -f == 0:
        x = i
        break

print(x,y)