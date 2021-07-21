# 함수명: print_gugudan, 매개변수: 1개, 리턴값: 없음
# 기능: 전달된 숫자의 구구단을 출력한다.
#       - 전달된 아규먼트가 int 타입인지 체크하고 int 타입이 아니면 그냥 리턴한다.
#       - 전달된 아규먼트가 1~9 사이인지 체크하고 아니면 그냥 리턴한다.
#       - 그 외의 경우에는 해당 단의 구구단을 행 단위로 출력한다.
def print_gugudan(num) :
    if type(num) != int :
        return
    elif 1 <= num <= 9 :
        for i in range(1, 10) :
            print(num, '*', i, '=', num * i)
    else :
        return

# 숫자를 다양하게 지정해서 print_gugudan() 함수를 호출해 본다.
print_gugudan(3)
print('-' * 10)
print_gugudan(4)
print('-' * 10)
print_gugudan(11)