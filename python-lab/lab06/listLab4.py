# 비어있는 리스트를 하나 생성하여 listnum 이라는 변수에 저장한다.
listnum = []
# 1~50 사이의 난수를 10개 추출하여 listnum에 추출 순서대로 저장한다.
import random
for _ in range(1, 11) :
    add_num = random.randint(1, 50)
    listnum.append(add_num)
# listnum의 모든 값들을 출력한다.
print(listnum)
# 리스트에서 10보다 작은 값들은 100으로 변경한다.
for i in range(0, len(listnum)) :
    if listnum[i] < 10 :
        listnum[i] = 100
print(listnum)
# 인덱싱 방법으로 listnum의 첫 번째 데이터를 출력한다.
print(listnum[0])
# 인덱싱 방법으로 listnum의 마지막 데이터를 출력한다.
print(listnum[-1]) # print(listnum[len(listnum)-1])
# 슬라이싱 방법으로 listnum의 두 번째 데이터부터 여섯 번째 데이터만 추출하여 출력한다.
print(listnum[1:6])
# 슬라이싱 방법으로 listnum의 데이터를 역순으로 출력한다.
print(listnum[::-1])
# 슬라이싱 방법으로 listnum의 데이터를 모두 출력한다.
print(listnum[::]) # print(listnum[:])
# 인덱싱 방법으로 5번째 데이터를 삭제한다.
del listnum[4]
# 슬라이싱 방법으로 listnum의 데이터를 모두 출력한다.
print(listnum[::])
# 슬라이싱 방법으로 2~3번째 데이터를 삭제한다.
listnum[1:3] = []
# 슬라이싱 방법으로 listnum의 데이터를 모두 출력한다.
print(listnum[::])
