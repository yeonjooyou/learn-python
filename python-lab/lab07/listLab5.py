# 비어있는 리스트를 하나 만들고
# 이 안에 1~45 사이의 난수를 추출하여 6개를 저장하는데, 이때 중복 불허한다.
lotto_list =[]
import random
while True :
    num = random.randint(1, 45)
    if num not in lotto_list :
        lotto_list.append(num)
        if len(lotto_list) == 6 :
            break
print('행운의 로또번호 :', *lotto_list)

'''
# case 2
lst = [] # list()
while len(lst) < 6 :
    num = random.randint(1, 45)
    if num not in lst :
        lst.append(num)  # append : list의 메서드

print("행운의 로또번호 : ", end = "")
for num in lst :
    print(num, end = " ")
print()
'''