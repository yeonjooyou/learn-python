# 함수명: sumEven1, 매개변수: 가변형, 리턴값: 1개
# 기능: 아규먼트가 몇 개가 전달되든 처리해야 한다.
#       아규먼트는 1 이상의 숫자만 온다고 정한다.
#       전달된 아규먼트들에서 짝수에 해당하는 숫자들만 합을 계산해서 리턴한다.
#       전달된 아규먼트들 중에서 짝수가 없으면 0을 리턴한다.
#       아규먼트가 전달되지 않으면 -1을 리턴한다.
def sumEven1(*ints) :
    sum = 0
    if not ints :
        return -1
    else :
        for num in ints :
            if num % 2 == 0 :
                sum += num
        return sum

print(sumEven1())
print(sumEven1(1, 3, 5, 7))
print(sumEven1(2, 3))
print(sumEven1(2, 3, 4))