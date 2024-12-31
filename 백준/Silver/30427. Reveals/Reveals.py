swi_message = input() # swi's cake is missing!
N = int(input())  # 집 안에 있던 사람 수
people_in_house = [input() for _ in range(N)]  # 집 안에 있던 사람들

M = int(input())  # 목격담의 수
witnessed_people = [input() for _ in range(M)]  # 목격된 사람들

# 목격담이 없는 사람 리스트 구하기
no_witness = [person for person in people_in_house if person not in witnessed_people]

# 규칙 처리
if "dongho" in people_in_house:
    print("dongho")  # 규칙 1
elif len(no_witness) == 1:
    print(no_witness[0])  # 규칙 2
elif "bumin" in no_witness:
    print("bumin")  # 규칙 3
elif "cake" in no_witness:
    print("cake")  # 규칙 4
elif "lawyer" in no_witness:
    print("lawyer")  # 규칙 5
elif no_witness:
    print(sorted(no_witness)[0])  # 규칙 6
else:
    print("swi") # 규칙 7