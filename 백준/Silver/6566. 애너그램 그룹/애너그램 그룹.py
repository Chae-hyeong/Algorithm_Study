from collections import defaultdict

# 입력 처리
words = []
while True:
    try:
        word = input().strip()
        words.append(word)
    except EOFError:
        break

# 애너그램 그룹화
groups = defaultdict(list)
for word in words:
    sorted_word = ''.join(sorted(word))
    groups[sorted_word].append(word)

# 중복 제거 및 정렬
filtered_anagrams = {
    k: [sorted(set(v)), len(v)] for k, v in groups.items()
}

# 그룹 정렬
sorted_anagrams = sorted(
    filtered_anagrams.items(),
    key=lambda item: (-item[1][1], item[1][0][0])  # 그룹 크기 내림차순, 첫 단어 사전 순
)

# 출력
for i in range(min(5, len(sorted_anagrams))):  # 상위 5개만 출력
    group_size = sorted_anagrams[i][1][1]
    group_words = " ".join(sorted_anagrams[i][1][0])
    print(f"Group of size {group_size}: {group_words} .")