def solution(arr, queries):
    for q in queries:
        i , j = q
        arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [0, 1, 2, 3, 4]
queries = [[0, 3],[1, 2],[1, 4]]
solution(arr, queries)