def can_form(sign, name):
    """
    오래된 간판 sign에서 일정한 간격으로 편의점 이름 name을 만들 수 있는지 확인
    """
    sign_length, name_length = len(sign), len(name)

    # 간판의 모든 시작 위치와 간격 탐색
    for start in range(sign_length):
        if sign[start] != name[0]:
            continue  # 첫 글자가 다르면 다음으로 넘어감

        for gap in range(1, sign_length):
            if start + (name_length - 1) * gap >= sign_length:
                break  # 간판 범위를 넘어가면 중단

            if all(sign[start + idx * gap] == name[idx] for idx in range(name_length)):
                return True  # 간격으로 편의점 이름을 만들 수 있음

    return False


def count_signs(N, name, signs):
    """
    주어진 간판들에서 일정한 간격으로 편의점 이름을 만들 수 있는 간판의 수
    """
    return sum(1 for sign in signs if can_form(sign, name))

# 입력 처리
N = int(input())
name = input().strip()
signs = [input().strip() for _ in range(N)]

print(count_signs(N, name, signs))