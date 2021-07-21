# 함수명: print_triangle, 매개변수: 1개, 리턴값: 없음
# 기능: 전달된 숫자 개수로 구성되는 삼각형을 출력한다.
def print_triangle(step) :
    # 전달되는 아규먼트 값은 1~10으로 제한한다.
    if 1 <= step <= 10 :
        for i in range(1, step+1) :
            print('*' * i)
    # 1~10 이외의 값이 전달된 경우에는 처리하지 않고 그냥 리턴한다.
    else :
        return

print_triangle(2)
print('-' * 10)
print_triangle(5)
print('-' * 10)
print_triangle(11)