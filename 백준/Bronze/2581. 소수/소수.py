import math

def get_prime_info(M, N):
    numbers = [True for _ in range(N + 1)]
    numbers[0] = numbers[1] = False

    for i in range(2, int(math.sqrt(N)) + 1):
        if numbers[i]:
            for p in range(i * i, N + 1, i):
                numbers[p] = False

    primes = [p for p in range(M, N + 1) if numbers[p]]

    if primes:
        return sum(primes), min(primes)
    else:
        return None


if __name__ == '__main__':
    M = int(input())
    N = int(input())

    result = get_prime_info(M, N)

    if result:
        print(*result, sep='\n')
    else:
        print(-1)