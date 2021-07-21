weather_dict = {
    '월' : (32, 24),
    '화': (33, 24),
    '수': (33, 25),
    '목': (33, 23),
    '금': (31, 23),
    '토': (31, 24),
    '일': (29, 24),
}
# 사용자에게 요일명 한 개를 입력받는다.
day = input("> 요일명을 한글로 입력하세요 :")
if day in weather_dict :
    print(day, '요일의 최저온도는', min(weather_dict[day]), '이고'
                    '최고온도는', max(weather_dict[day]), '도 입니다.')

else :
    print(day, '요일의 정보를 찾을 수 없습니다.')
