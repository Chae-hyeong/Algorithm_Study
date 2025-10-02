import sys
input = sys.stdin.readline

n = int(input())
books = sorted([input().strip() for _ in range(n)])
names = sorted(list(set(books)))
count = []

for name in names:
    count.append(books.count(name))

print(names[count.index(max(count))])