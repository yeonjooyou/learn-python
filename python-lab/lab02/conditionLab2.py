# 1. color_name 이라는 변수에 사용자로부터 칼라 이름을 하나 입력받는다.
color_name = input("색 이름: ")
# 2. 입력받은 칼라명이 red 이면 '#ff0000'라는 문자열을 출력한다.
if color_name == "red": # color_name == red 는 red라는 변수로 인식
    print("#ff0000")
#    입력받은 칼라명이 red 가 아니면 '#000000'라는 문자열을 출력한다.
else: # if color_name != "red":
    print("#000000")