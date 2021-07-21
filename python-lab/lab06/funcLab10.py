# 함수명: sumAll, 매개변수: 가변형, 리턴값: 1개
# 기능: 아규먼트가 몇 개 전달되든 처리해야 한다.
#       호출 시 전달되는 아규먼트의 데이터 타입에는 제한이 없다.
#       그러므로 전달된 아규먼트의 타입을 체크하여 숫자만 처리하고 숫자가 아닌 데이터는 무시한다.
#       아규먼트가 전달되지 않았거나 전달되었다 하더라도 숫자가 없으면 None을 리턴한다.
def sumAll(*ints) :
    sum = 0 # sum = None 인 경우 덧셈연산 불가능!!
    for num in ints :
        if not ints: # len()함수 이용해도 됨
            return None
        elif type(num) == int :
            sum += num
    if sum == 0 : # 아규먼트로 문자만 전달되는 경우
        return None
    return sum

print(sumAll())
print(sumAll('-'))
print(sumAll(0, 'a'))
print(sumAll(1, '-'))
print(sumAll(1, 2, 3, '*', '^', 1.1, 6))