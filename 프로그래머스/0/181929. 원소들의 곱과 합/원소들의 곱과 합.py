#원소들의 곱과 합
from functools import reduce

def solution(num_list):
    num_sum = sum(num_list)**2
    num_mul = reduce(lambda x, y : x * y , num_list)
    if num_sum > num_mul:
        return 1
    else:
        return 0
    
    answer = 0
    return answer