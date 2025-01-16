import sys
input = sys.stdin.readline

# 균형 3진법
def base3(n):
    if n == 0:
        return "0"
    
    result = []

    while n != 0:
        remain = n % 3
        n //= 3  # 3으로 나눈 몫

        if remain == 2:  # 2일 경우 -1로 변환
            remain = -1
            n += 1  # 자리 올림 (몫 증가)

        if remain == -1:
            result.append("-")
        else:
            result.append(str(remain))

    return ''.join(result[::-1])  # 뒤집어서 반환

T = int(input())

for _ in range(T):
    n = int(input())
    print(base3(n))