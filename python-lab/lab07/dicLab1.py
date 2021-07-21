# https://www.w3schools.com/colors/colors_picker.asp
color_dict = {
    "red" : "#ff0000",
    "blue": "#0000ff",
    "green": "#005000",
    "yellow": "#ffff00",
    "orange": "#ffa500",
    "black": "#000000",
    "white": "#ffffff",
    "violet": "#ee82ee",
    "pink": "#ffc0cb",
    "lime": "#00ff00",
}

# 사용자에게 칼라명 한 개를 입력받는다.
color = input("> 칼라명을 영문으로 입력하세요 :")

if color in color_dict :
    print(color, '칼라의 RGB 값은', color_dict[color], '입니다.')
else :
    print(color, '칼라의 RGB 값을 찾을 수 없습니다.')