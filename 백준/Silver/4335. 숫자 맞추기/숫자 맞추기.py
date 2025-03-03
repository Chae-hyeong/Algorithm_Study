import sys
input = sys.stdin.readline

low, high = 1, 10

while True:
    guess = int(input())
    if guess == 0:
        break
    response = input().strip()

    if response == 'too high':
        high = min(high, guess - 1)
    elif response == 'too low':
        low = max(low, guess + 1)
    elif response == 'right on':
        if low <= guess <= high:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")
        low, high = 1, 10