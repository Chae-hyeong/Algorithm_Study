def solution(a, b, c):
    Dice = list(set([a, b, c]))
    same_count = len(Dice)
    if same_count == 1:
        return  ((a) * (a**2) * (a**3))*27
    elif same_count == 2:
        return (a + b + c) * (a**2 + b**2 + c**2 )
    else:
        return a+b+c