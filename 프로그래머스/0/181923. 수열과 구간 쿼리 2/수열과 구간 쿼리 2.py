def solution(arr, queries):
    result = []

    for s, e, k in queries:
        valid_elements = [element for element in arr[s:e+1] if element > k]
        result.append(min(valid_elements) if valid_elements else -1)

    return result

