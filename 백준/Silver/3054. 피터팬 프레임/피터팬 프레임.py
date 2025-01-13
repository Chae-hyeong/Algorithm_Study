# 입력 단어
s = input()

# 1, 5번째 줄 생성
for i in range(len(s)):
    if (i + 1) % 3 == 0:
        print("..*.", end="")
    else:
        print("..#.", end="")
    if i == len(s) - 1:
        print(".")

# 2, 4번째 줄 생성
for i in range(len(s)):
    if (i + 1) % 3 == 0:
        print(".*.*", end="")
    else:
        print(".#.#", end="")
    if i == len(s) - 1:
        print(".")

# 3번째 줄 생성
for i in range(len(s)):
    if i > 0 and i % 3 == 0 or (i + 1) % 3 == 0:
        print("*", end="")
    else:
        print("#", end="")
    if (i + 1) % 3 == 0:
        print(f".{s[i]}.", end="")
    else:
        print(f".{s[i]}.", end="")
    if i == len(s) - 1:
        if (i + 1) % 3 == 0:
            print("*")
        else:
            print("#")

# 2, 4번째 줄 생성 (반복)
for i in range(len(s)):
    if (i + 1) % 3 == 0:
        print(".*.*", end="")
    else:
        print(".#.#", end="")
    if i == len(s) - 1:
        print(".")

# 1, 5번째 줄 생성 (반복)
for i in range(len(s)):
    if (i + 1) % 3 == 0:
        print("..*.", end="")
    else:
        print("..#.", end="")
    if i == len(s) - 1:
        print(".")