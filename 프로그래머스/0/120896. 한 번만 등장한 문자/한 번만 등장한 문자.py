def solution(s):
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0)+1
    result = [char for char, count in char_count.items() if count == 1]
    return "".join(sorted(result))