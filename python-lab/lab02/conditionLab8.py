# 1. oper_num 이라는 변수에 1부터 10사이의 랜덤값을 추출하여 대입한다.
import random
oper_num = random.randint(1, 10)
print("랜덤값: ", oper_num) #랜덤값을 확인하기 위한 출력문
a = 300
b = 50
# 추출된 값이 1이거나 6이면 덧셈 연산을 처리한다.
if oper_num == 1 or oper_num == 6:
    c = a + b
# 추출된 값이 2이거나 7이면 뺄셈 연산을 처리한다.
elif oper_num == 2 or oper_num == 7:
    c = a - b
# 추출된 값이 3이거나 8이면 곱셈 연산을 처리한다.
elif oper_num == 3 or oper_num == 8:
    c = a * b
# 추출된 값이 4이거나 9이면 나눗셈 연산을 처리한다.
elif oper_num == 4 or oper_num == 9:
    c = a / b
# 추출된 값이 5이거나 10이면 나머지 연산을 처리한다.
else:
    c = a % b
# 결과를 출력하는 수행문장은 한 번만 구현한다.
print("결과값: ", c)