import sys
from collections import Counter

input = sys.stdin.readline

n, m = map(int, input().split())
people = sorted([input().strip() for _ in range(n+m)])
result = []
counter = Counter(people).most_common()

for i in range(len(counter)):
    if counter[i][1] >= 2:
        result.append(counter[i][0])

print(len(result))
print(*result, sep='\n')