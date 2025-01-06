def word_similar(word, typo):
    # 한 글자 추가/삭제
    if abs(len(word) - len(typo)) == 1:
        for i in range(min(len(word), len(typo))):
            if word[i] != typo[i]:
                return word[i:] == typo[i+1:] or word[i+1:] == typo[i:]
        return True

    # 한 글자 교체
    if len(word) == len(typo):
        diff_count = sum(1 for char1, char2 in zip(word, typo) if char1 != char2)
        if diff_count == 1:
            return True

    # 순서 뒤집힘
    if len(word) == len(typo):
        for i in range(len(word) - 1):
            if (typo[:i] + typo[i + 1] + typo[i] + typo[i + 2:]) == word:
                return True

    return False

# 입력 처리
N = int(input())
word_list = [input().strip() for _ in range(N)]

q = int(input())
typos = [input().strip() for _ in range(q)]

# 결과 처리
for typo in typos:
    # 단어 사전에 있는 단어인 경우
    if typo in word_list:
        print(f"{typo} is correct")
    else:
        similar_word = None
        for word in word_list:
            # 비슷한 단어 찾기
            if word_similar(word, typo):
                similar_word = word
                break

        if similar_word:
            print(f"{typo} is a misspelling of {similar_word}")
        else:
            print(f"{typo} is unknown")
