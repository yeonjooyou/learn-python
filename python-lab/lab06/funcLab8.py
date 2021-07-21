# 함수명: print_triangle_withdeco, 매개변수: 2개, 리턴값: 없음
# 기능: 전달된 숫자 개수로 구성되는 삼각형을 출력한다.
# 기본값을 갖는 매개변수의 함수 정의하기
def print_triangle_withdeco(num, deco = '%') :
    if 1 <= num <= 10 :
        for i in range(1, num+1) :
            print(' ' * (num - i), end ='')
            print(deco * i)

# 숫자 2만 전달 시
print_triangle_withdeco(2)
print('-' * 10)
# 숫자 5와 데코문자 '*' 전달 시
print_triangle_withdeco(5, '*')