def mod_exp(a, b, c):
    if b == 0:
        return 1
    elif b % 2 == 0:
        half = mod_exp(a, b // 2, c)
        return (half * half) % c
    else:
        return (a * mod_exp(a, b - 1, c)) % c

A, B, C = map(int, input().split())
print(mod_exp(A, B, C))