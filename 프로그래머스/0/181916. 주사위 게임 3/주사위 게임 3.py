from collections import Counter

def solution(a, b, c, d):
    cnt = [(key, value) for key, value in Counter([a, b, c, d]).items()]
    cnt = sorted(cnt, key=lambda x: -x[1])
    if cnt[0][1] == 4:
        return 1111 * a
    elif cnt[0][1] == 3:
        return ((10 * cnt[0][0]) + cnt[1][0]) ** 2
    elif cnt[0][1] == 2:
        if cnt[1][1] == 2:
            return (cnt[0][0] + cnt[1][0]) * abs(cnt[0][0] - cnt[1][0])
        return cnt[1][0] * cnt[2][0]
    return min(a, b, c, d)