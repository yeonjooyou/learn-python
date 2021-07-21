# 함수명: expr, 매개변수: 숫자 2개와 연산자 1개, 리턴값: 연산 결과 또는 None
# 기능: 전달된 두 개의 숫자에 대해서 전달된 연산을 처리하고 그 결과를 리턴한다.
#       연산자는 +,-,*,/ 만 처리하며 그 외의 연산자는 연산을 하지 않고 None 값을 리턴한다.
def expr(a, b, operator) :
    if operator == '+' :
        return a + b
    elif operator == '-' :
        return a - b
    elif operator == '*' :
        return a * b
    elif operator == '/' :
        return a / b
    else :
        return None

# 숫자 2개와 연산자 1개를 전달하여 expr()이라는 함수를 호출한 다음
# 리턴 결과가 None이면 '수행불가'를 출력하고
# 그렇지 않으면 '연산결과 : XX'를 출력한다.
'''
# case1
a = int(input('a = '))
b = int(input('b = '))
operator = input('operator : ')

if expr(a, b, operator) != None :
    print('연산결과 :', expr(a, b, operator))
else :
    print('수행 불가')
'''

# case2. hard coding
result = expr(1, 2, '+')
if result != None :
    print('연산결과 :', result)
else :
    print('수행 불가')