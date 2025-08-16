x, y = map(int, input().split())
d = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(x - 1):
    y += month[i]

print(d[(y%7)])
