import sys
input = sys.stdin.readline

color = set()
for _ in range(2):
    tmp = input().rstrip().split()
    for i in tmp:
        color.add(i)

color_list = sorted(list(color))

for i in color_list:
    for j in color_list:
        print(i, j)