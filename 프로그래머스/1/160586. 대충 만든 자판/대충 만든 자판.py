def solution(keymap, targets):
    answer = []
    key_dict = {}
    
    for i in keymap: 
        for idx, char in enumerate(i):
            if char not in key_dict:
                key_dict[char] = (idx+1)
            else: 
                key_dict[char] = min(key_dict[char],(idx+1))
    
    for i in targets: 
        count = 0
        for j in i:
            if j not in key_dict:
                count = -1
                break
            count += key_dict[j]
        answer.append(count)
    
    return answer