# 10, 5, 7, 21, 4, 8, 18 로 구성되는 리스트를 생성하여 listnum에 저장한다.
listnum = [10, 5, 7, 21, 4, 8, 18]
# listnum에 저장된 값들 중에서 최댓값을 추출하여 출력한다.
# 최대값을 구하는 기능은 함수를 사용하지 않고 제어문으로 직접 구현한다.
max_value = listnum[0]
for i in range(1, len(listnum)) :
    if max_value < listnum[i] :
        max_value = listnum[i]
print('최댓값 :', max_value)