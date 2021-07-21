str_list = [['B', 'C', 'A', 'A'],
            ['C', 'C', 'B', 'B'],
            ['D', 'A', 'A', 'D']]
# 다음 내용으로 구성되는 리스트를 하나 생성한다.
# case 1 _ 함수를 통해 각각의 문자 카운트 하기(count 메소드 사용)
count_list = []
def count (str) :
    sum = 0
    for i in range(0, 3) :
        sum += str_list[i].count(str)
    count_list.append(sum)
# 첫 번째 원소에는 'A' 문자의 개수
count('A')
# 두 번째 원소에는 'B' 문자의 개수
count('B')
# 세 번째 원소에는 'C' 문자의 개수
count('C')
# 네 번재 원소에는 'D' 문자의 개수
count('D')

# print(count_list)
print('case1 출력문 입니다.')
print('A는', count_list[0], '개 입니다.')
print('B는', count_list[1], '개 입니다.')
print('C는', count_list[2], '개 입니다.')
print('D는', count_list[3], '개 입니다.')

# case 2 _ 중첩 for문을 통해 각각의 문자 카운트하기
A, B, C, D = 0, 0, 0, 0
for i in range(0, 3) :
    for j in range(0, 4) :
        if str_list[i][j] == 'A' :
            A += 1
        elif str_list[i][j] == 'B' :
            B += 1
        elif str_list[i][j] == 'C' :
            C += 1
        elif str_list[i][j] == 'D' :
            D += 1
    count_list.extend([A, B, C, D]) # list에 여러 항목 추가하기

print('case2 출력문 입니다.')
for i in range(4) :
    print(chr(65+i), '는 ', count_list[i], '개 입니다.', sep='')

# case 3
data = {0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D'}
count_lst = []
for d in data.values() : # for _, d in data.items() :
    count = 0
    for row in str_list :
        count += row.count(d)
    count_lst.append(count)

for i, d in data.items() :
    print(d, '는 ', count_lst[i], '개 입니다.', sep='')



'''
# Error Code _ 이차원 list에서는 인덱스를 행단위로 인식
# 첫 번째 원소에는 'A' 문자의 개수
count_list.append(str_list.count('A'))
# 두 번째 원소에는 'B' 문자의 개수
count_list.append(str_list.count('B'))
# 세 번째 원소에는 'C' 문자의 개수
count_list.append(str_list.count('C'))
# 네 번재 원소에는 'D' 문자의 개수
count_list.append(str_list.count('D'))

print('A는', count_list[0], '개 입니다.')
print('B는', count_list[1], '개 입니다.')
print('C는', count_list[2], '개 입니다.')
print('D는', count_list[3], '개 입니다.')
'''