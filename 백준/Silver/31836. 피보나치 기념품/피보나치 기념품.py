N = int(input())

A, B = [], []
i = N
while i > 2:
    A.append(i)
    B.append(i - 1)
    B.append(i - 2)
    i -= 3

if N % 3 == 2:
    A.append(1)
    B.append(2)

print(len(A))
print(*A)
print(len(B))
print(*B)