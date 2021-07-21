# 10, 5, 7, 21, 4, 8, 18 로 구성되는 리스트를 생성하여 listnum에 저장한다.
listnum = [10, 5, 7, 21, 4, 8, 18]
# listnum에 저장된 값들 중에서 최솟값을 추출하여 출력한다.
# 최솟값을 구하는 기능은 함수를 사용하지 않고 제어문으로 직접 구현한다.
min_value = listnum[0]
for i in range(1, len(listnum)) :
    if min_value > listnum[i] :
        min_value = listnum[i]
print('최솟값 :', min_value)