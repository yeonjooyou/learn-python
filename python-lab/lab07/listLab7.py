list = [[10, 20, 30, 40, 50],
        [5, 10, 15],
        [11, 22, 33, 44],
        [9, 8, 7, 6, 5, 4, 3, 2, 13]]
# 행단위 합을 구하여 출력한다.
def sumRow(order) :
        sum = 0
        for i in range(0, len(list[order])) :
                sum += list[order][i]
        print(order+1, '행의 합은', sum, '입니다.')

for order in range(0, 4) :
        sumRow(order)

# case 2
for row in range(len(list)) :
        row_sum = 0
        for col in list[row] :
                row_sum += col
        print(row + 1, '행의 합은 ', row_sum, '입니다.', sep = '')
'''
sum1 = 0
for i in range(0, len(list[0])) :
        sum1 += list[0][i]
print('1행의 합은', sum1, '입니다.')

sum2 = 0
for i in range(0, len(list[1])) :
        sum2 += list[1][i]
print('2행의 합은', sum2, '입니다.')

sum3 = 0
for i in range(0, len(list[2])) :
        sum3 += list[2][i]
print('3행의 합은', sum3, '입니다.')

sum4 = 0
for i in range(0, len(list[3])) :
        sum4 += list[3][i]
print('4행의 합은', sum4, '입니다.')
'''