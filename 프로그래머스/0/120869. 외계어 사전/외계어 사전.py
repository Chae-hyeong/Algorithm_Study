def solution(spell, dic):
    a = min([1 if sorted(x) == sorted(spell) else 2 for x in dic])
    return a