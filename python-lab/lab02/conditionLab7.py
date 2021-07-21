# 1. num 이라는 변수에 사용자로부터 숫자 하나를 입력받는다.
num = input('1부터 10사이의 숫자를 하나 입력하세요: ')
# 2. 입력 받은 숫자가 1부터 10사이의 숫자가 아니면
if 1 > int(num) or int(num) >10:
    print("1부터 10사이의 값이 아닙니다.")
# 3. 입력 받은 숫자가 1부터 10사이의 숫자이면
else:
    if int(num) % 2 == 0:
        print(num, ": 짝수", sep="")
    else:
        print(num, ": 홀수", sep="")