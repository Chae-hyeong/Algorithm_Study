def solution(wallet, bill):
    answer = 0
    while (min(wallet) < min(bill) or max(wallet) < max(bill)):
        bill[bill.index(max(bill))] = int(max(bill)/2)
        answer += 1
    
    
    return answer