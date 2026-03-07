def solution(bandage, health, attacks):
    hp = health
    t = 0
    t_end = attacks[-1][0]
    bt = bandage[0]
    
    while t < t_end:
        t += 1
        
        if t == attacks[0][0]:
            hp -= attacks[0][1]
            attacks.pop(0)
            bt = bandage[0]
            
            if hp <= 0: return -1
            continue
    
        if hp < health:      
            if bt == 1: hp += bandage[2]
            hp += bandage[1]
            
            bt -= 1
            if bt == 0 and hp < health: bt = bandage[0]
            
            if hp > health: hp = health
        
    return hp