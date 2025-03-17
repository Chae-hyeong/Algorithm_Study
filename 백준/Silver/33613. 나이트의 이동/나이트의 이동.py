n = int(input())
r, c = map(int, input().split())

directions = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]

can_move = False
for dr1, dc1 in directions:
    nr, nc = r + dr1, c + dc1
    if 1 <= nr <= n and 1 <= nc <= n:
        for dr2, dc2 in directions:
            nnr, nnc = nr + dr2, nc + dc2
            if 1 <= nnr <= n and 1 <= nnc <= n:
                can_move = True
                break
        if can_move:
            break

if not can_move:
    print(1)
else:
    if n == 3:
        print(4)  
    elif n % 2 == 0:
        print((n * n) // 2)
    else:
        if (r + c) % 2 == 0:
            print((n * n + 1) // 2)
        else:
            print((n * n - 1) // 2)