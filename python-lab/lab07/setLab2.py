# 비어있는 셋을 하나 만들고 이 안에 1~45 사이의 난수를 추출하여 6개를 저장한다.
import random

random_set = set()
while True :
    random_set.add(random.randint(1, 45))
    if len(random_set) == 6 :
        break
print('행운의 로또번호 :', random_set)


# case 2
s = set()
while len(s) < 6 :
    s.add(random.randint(1, 45)) # add : set의 메서드

print('행운의 로또번호 : ', end = "")
for d in s :
    print(d, end = " ")