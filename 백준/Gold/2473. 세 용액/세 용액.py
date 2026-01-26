import sys

def find_three_solutions(n, arr):
    arr.sort()
    min_sum = float('inf')
    result = []

    for i in range(n - 2):
        start = i + 1
        end = n - 1

        while start < end:
            current_sum = arr[i] + arr[start] + arr[end]

            if abs(current_sum) < abs(min_sum):
                min_sum = current_sum
                result = [arr[i], arr[start], arr[end]]

            if current_sum == 0:
                return result
            elif current_sum < 0:
                start += 1
            else:
                end -= 1

    return result


if __name__ == "__main__":
    input = sys.stdin.readline

    n = int(input())
    arr = list(map(int, input().split()))

    print(*find_three_solutions(n, arr))