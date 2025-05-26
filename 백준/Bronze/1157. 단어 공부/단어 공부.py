from collections import Counter

word = input().upper()
counter = Counter(word)
most_common = counter.most_common(2)

if len(most_common) == 1 or most_common[0][1] != most_common[1][1]:
    print(most_common[0][0])
else:
    print("?")