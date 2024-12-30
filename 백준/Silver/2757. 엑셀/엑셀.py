# 숫자와 알파벳 매핑
number_to_alpha = {i: chr(64 + i) for i in range(1, 27)}

while True:
    cell = input()
    if cell == "R0C0":
        break
    n, m = cell[1:cell.index('C')], int(cell[cell.index('C')+1:])
    # 숫자 m을 알파벳으로 변환 (26진법)
    result = []
    while m > 0:
        r = m % 26
        if r == 0:  # 나머지가 0일 때 Z 처리
            result.append('Z')
            m = m // 26 - 1
        else:
            result.append(number_to_alpha[r])
            m //= 26
    # 결과 출력 (알파벳은 역순이므로 뒤집기)
    print(''.join(reversed(result)) + str(n))