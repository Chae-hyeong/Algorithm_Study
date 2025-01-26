import sys
input = sys.stdin.readline

# 초콜릿 종류 및 입력 처리
choco_types = ['H', 'T', 'C', 'K', 'G']
chocolates = list(map(int, input().split()))

# 초콜릿 총합 계산
total_sum = sum(chocolates)

# 초콜릿 먹는 횟수
M = int(input())

output = []
last_digit = total_sum % 10  # 첫 번째 총합의 일의 자리

# 초콜릿 먹는 과정
for i in range(M):
    eaten = list(map(int, input().split()))

    # 초콜릿 개수 업데이트
    for j in range(5):
        chocolates[j] = max(0, chocolates[j] - eaten[j])

    # 총 개수 계산
    total_sum = sum(chocolates)

    # 진법 변환
    base = last_digit if last_digit not in (0, 1) else 10
    converted_total = ""
    num = total_sum

    # 진법 변환
    if num == 0:
        converted_total = "0"
    else:
        while num > 0:
            converted_total = str(num % base) + converted_total
            num //= base

    output.append(f"{converted_total}7H")

    # 남은 초콜릿 개수 정렬
    remaining = [(choco_types[j], chocolates[j]) for j in range(5) if chocolates[j] > 0]

    if not remaining:
        output.append("NULL")
    else:
        remaining.sort(key=lambda x: (-x[1], x[0]))  # 개수 내림차순, 알파벳 오름차순
        output.append("".join([x[0] for x in remaining]))

    # 현재 총합의 일의 자리 저장
    last_digit = total_sum % 10

# 결과 출력
print("\n".join(output))