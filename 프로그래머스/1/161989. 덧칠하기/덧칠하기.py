def solution(n, m, section):
    answer = 0
    
    #롤러를 왼쪽에서부터 오른쪽으로 움직이면서 색칠한다.
    #end = 롤러의 오른쪽 끝
    end = 0
    
    for sect in section:
        #이미 칠해진 부분이면 pass
        if sect <= end:
            pass
        else:
            #칠해져있지 않은 부분이지만 끝자락에 있어서 
            #롤러를 움직였을 때 벽에서 벗어나면 answer += 1하고 리턴
            if sect + m -1 > n:
                return answer + 1
            #아니라면 end = sect + m -1로 이동(sect가 맨 왼쪽에 오게 m만큼 색칠)
            else:
                end = sect + m -1
                answer += 1
    return answer