def solution(num_list):
    odd = ''.join(map(str, [x for x in num_list if x % 2 != 0]))
    even = ''.join(map(str, [x for x in num_list if x % 2 == 0]))
    return int(even) + int(odd)