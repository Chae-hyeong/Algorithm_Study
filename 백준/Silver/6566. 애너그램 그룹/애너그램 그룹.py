from collections import defaultdict

# 입력 처리
words = []  # 입력된 단어를 저장할 리스트
while True:
    try:
        word = input()
        words.append(word)
    except EOFError:
        break

# 애너그램 그룹화
anagram_groups = defaultdict(list)  # 정렬된 단어를 키로 하는 애너그램 그룹
for word in words:
    sorted_word = ''.join(sorted(word))  # 단어를 정렬하여 키로 사용
    anagram_groups[sorted_word].append(word)

# 중복 제거 및 정렬
processed_groups = {
    key: [sorted(set(words)), len(words)]  # 중복 제거, 사전순 정렬, 그룹 크기 저장
    for key, words in anagram_groups.items()
}

# 그룹 정렬
sorted_groups = sorted(
    processed_groups.items(),
    key=lambda group: (-group[1][1], group[1][0][0])  # 그룹 크기 내림차순, 첫 단어 사전 순
)

# 결과 출력
top_groups = sorted_groups[:min(5, len(sorted_groups))]  # 상위 5개 그룹 선택
for group in top_groups:
    group_size = group[1][1]  # 그룹 크기
    sorted_words = " ".join(group[1][0])  # 사전순으로 정렬된 단어
    print(f"Group of size {group_size}: {sorted_words} .")