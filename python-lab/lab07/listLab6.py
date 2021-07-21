# 이차원 리스트(4*4_정방행렬)를 생성한다.
list = [[10, 12, 14, 16],
        [18, 20, 22, 24],
        [26, 28, 30, 32],
        [34, 36, 38, 40]]
# 1
print('1행 1열의 데이터 :', list[0][0])
# 2
print('3행 4열의 데이터 :', list[2][3])

# 3
print('행의 갯수 :', len(list))
# 4
print('열의 갯수 :', len(list[0]))

# 5
print('3행의 데이터들 :', *list[2]) # unpacking연산자 : *
# 5_case2
print('3행의 데이터들 : ', end = '')
for i in list[2] :
    print(i, end = ' ')
print()

# 6
column = []
for i in range(0, 4) :
    column.append(list[i][1])
    i += 1
print('2열의 데이터들 :', *column)
# 6_case2
print('2열의 데이터들 : ', end ='')
for i in range(len(list)) :
    print(list[i][1], end = ' ')
print()

# 7
left_diagonal_matrix = []
for i in range(0, 4) :
    left_diagonal_matrix.append(list[i][i])
    i += 1
print('왼쪽 대각선 데이터들 :', *left_diagonal_matrix)
# 7_case2
print('왼쪽 대각선 데이터들 : ', end = '')
for i in range(len(list)) :
    print(list[i][i], end = ' ')
print()

# 8
print('오른쪽 대각선 데이터들 :',
      list[0][3], list[1][2], list[2][1], list[3][0])
# 8_case2
print('오른쪽 대각선 데이터들 : ', end = '')
for i in range(len(list)) :
    print(list[i][len(list)-1-i], end = ' ')
print()