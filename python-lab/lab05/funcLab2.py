# 함수명: get_book_title, 매개변수: 없음, 리턴값: 있음
# 기능: 파이썬 교재명을 리턴한다.
def get_book_title() :
    return '파이썬 정복'
# 함수명: get_book_publisher, 매개변수: 없음, 리턴값: 있음
def get_book_publisher() :
    return '한빛미디어'

# get_book_title() 함수를 호출하고 리턴되는 결과를 name 변수에 저장한 다음
name = get_book_title()
# name 변수의 값을 2회 출력한다.
print(name)
print(name)
'''
# case2
for _ in range(2) :
    print(name)
'''

# get_book_publisher() 함수를 호출하고 리턴되는 결과를 화면에 출력한다.
print(get_book_publisher())