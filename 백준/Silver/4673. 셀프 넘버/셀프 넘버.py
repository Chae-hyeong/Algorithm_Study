def get_self_numbers(limit=10000):
    is_self_number = [True] * limit

    for n in range(1, limit + 1):
        generated = n + sum(int(digit) for digit in str(n))

        if generated <= limit:
            is_self_number[generated - 1] = False

    return [i + 1 for i in range(limit) if is_self_number[i]]


if __name__ == "__main__":
    for num in get_self_numbers():
        print(num)