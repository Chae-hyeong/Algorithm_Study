from itertools import permutations

X = input()
X_num = int(X)

perms = sorted([int(''.join(perm)) for perm in permutations(X, len(X)) if perm[0] != '0'])

start, end = 0, len(perms) - 1
result = 0

while start <= end:
    mid = (start + end) // 2
    if perms[mid] <= X_num:
        start = mid + 1
    else:
        result = perms[mid]
        end = mid - 1

print(result)