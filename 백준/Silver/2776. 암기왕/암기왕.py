import sys
input = sys.stdin.readline

# 이분 탐색 함수
def binary_search(note1, num):
    left, right = 0, len(note1) - 1
    while left <= right:
        mid = (left + right) // 2
        if note1[mid] == num:
            return True
        elif note1[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return False

# 테스트 케이스 수
T = int(input())

for _ in range(T):
    # 수첩 1
    N = int(input())
    note1 = list(map(int, input().split()))
    note1.sort()  # 수첩 1 정렬

    # 수첩 2
    M = int(input())
    note2 = list(map(int, input().split()))

    # 수첩 2의 각 숫자에 대해 탐색
    for num in note2:
        if binary_search(note1, num):
            print(1)
        else:
            print(0)