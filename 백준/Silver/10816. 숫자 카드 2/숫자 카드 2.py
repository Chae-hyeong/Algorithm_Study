import sys
from collections import Counter

input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
arr1 = list(map(int, input().split()))
counter = Counter(arr1)

M = int(input())
arr2 = list(map(int, input().split()))

write(' '.join(str(counter[x]) for x in arr2))