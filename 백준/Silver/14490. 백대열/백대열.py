n, m = map(int, input().split(':'))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

t = gcd(max(n, m), min(n, m))
print(f'{n // t}:{m // t}')