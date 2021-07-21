# 함수명: differ_two_value, 매개변수: 2개, 리턴값: 연산결과
# 기능: 전달받은 2개의 데이터 중에서 큰 값에서 작은 값의 차를 리턴 두 값이 동일하면 0을 출력한다.
#       10, 20이 전달되면 -> 10 리턴
#       20, 5이 전달되면 -> 15 리턴
#       5, 30이 전달되면 -> 25 리턴
#       6, 3이 전달되면 -> 3 리턴
def differ_two_value(X, Y) :
    if X > Y :
        return X - Y
    elif X < Y :
        return Y - X
    else :
        return 0
'''
# 함수정의 case2. 내장함수 abs() 이용
def differ_two_value(X, Y):
    if X != Y :
        return abs(X-Y)
    else :
        return 0
'''

# 1부터 30 사이의 난수 2개를 추출하여 2번에서 구현된 함수를 호출하고 결과를 출력한다.
import random
"""
X = random.randint(1, 30)
Y = random.randint(1, 30)
print('X :', X, ', Y :', Y)
print('X와 Y의 차는 ', differ_two_value(X, Y), '입니다.')
"""
def print_differ_two_value():
    X = random.randint(1, 30)
    Y = random.randint(1, 30)
    # X, Y = random.randint(1, 30), random.randint(1,30)
    print('X :', X, ', Y :', Y)
    print('X와 Y의 차는 ', differ_two_value(X, Y), '입니다.')

print_differ_two_value()
print_differ_two_value()
print_differ_two_value()
print_differ_two_value()
print_differ_two_value()

'''
# 출력 case2
for _ in range(5) :
    print_differ_two_value()
'''