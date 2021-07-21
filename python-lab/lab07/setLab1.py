# 비어있는 셋을 2개 만들고 각각 1~20 사이의 숫자 10개를 추출하여 저장한다.
import random # from random import randint
set1 = set()
set2 = set()

while True :
    set1.add(random.randint(1, 20))
    if len(set1) == 10 :
        break
while True :
    set2.add(random.randint(1, 20))
    if len(set2) == 10 :
        break

'''
# 랜덤값 추출 중 중복된 랜덤값이 있는 경우 10개가 추출이  안된다.
for _ in range(10) :
    set1.add(random.randint(1,20))
    set2.add(random.randint(1, 20))
'''

# 생성된 2개의 셋에 대하여 집합 연산을 수행하고 결과를 출력한다.
print('집합 1:', set1)
print('집합 2:', set2)

print('두 집합에 모두 있는 데이터 :', set1 & set2)
print('집합1 또는 집합2에 있는 데이터 :', set1 | set2)
print('집합1에는 있고 집합2에는 없는 데이터 :', set1 - set2)
print('집합2에는 있고 집합1에는 없는 데이터 :', set2 - set1)
print('집합1과 집합2가 각자 가지고 있는 데이터 :', set1 ^ set2)