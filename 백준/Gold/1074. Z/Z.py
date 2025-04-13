
def z(n, r, c):
    if n == 0:
        return 0

    half = 2 ** (n-1)
    block_size = half * half

    if r < half and c < half: # 1사분면
        return z(n-1, r, c)
    elif r < half and c >= half: # 2사분면
        return block_size + z(n-1, r, c - half)
    elif r >= half and c < half: # 3사분면
        return 2 * block_size + z(n-1, r - half, c)
    else: # 4사분면
        return 3 * block_size + z(n-1, r - half, c - half)

N, r, c = map(int, input().split())
print(z(N, r, c))