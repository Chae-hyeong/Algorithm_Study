def solution(mats, park):
    answer = -1
    mats = sorted(mats)
    for i in range(len(park)):
        for j in range(len(park[0])):
            for mat in mats:
                if i + mat > len(park) or j + mat > len(park[0]):
                    break
                if all(cell == '-1' for row in park[i:i+mat] for cell in row[j:j+mat]):
                    answer = max(mat, answer)
                else:
                    break    
    return answer