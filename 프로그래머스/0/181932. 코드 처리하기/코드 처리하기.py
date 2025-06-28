def solution(code):
    code = list(code)
    ret = ''
    mode = 0
    for idx, a in enumerate(code):
        if mode == 0:
            if a != '1':
                if idx % 2 == 0:
                    ret += a
            else:
                mode = 1
        elif mode == 1:
            if a != '1':
                if idx % 2 != 0:
                    ret += a
            else:
                mode = 0
    if ret == '':
        return "EMPTY"
    else:
        return ret

code = "abc1abc1abc"
solution(code)