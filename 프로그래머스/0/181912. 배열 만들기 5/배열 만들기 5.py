def solution(intStrs, k, s, l):
    answer = []
    for x in intStrs:
        num = int(x[s:s+l])
        if num > k:
            answer.append(num)
    return answer
