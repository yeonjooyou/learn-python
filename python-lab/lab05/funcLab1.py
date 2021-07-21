# 함수명: print_book_title, 매개변수: 없음, 리턴값: 없음
# 기능: 파이썬 교재명을 화면에 출력
def print_book_title() :
    print('파이썬 정복')
# 함수명: print_book_publisher, 매개변수: 없음, 리턴값: 없음
# 기능: 파이썬 교재의 출판사명을 화면에 출력
def print_book_publisher() :
    print('한빛미디어')

# print_book_title() 함수를 3회 호출하고
print_book_title()
print_book_title()
print_book_title()
'''
# case2
for _ in range(3) :
    print_book_title()
'''
# print_bookr_publisher() 함수를 5회 호출한다.
print_book_publisher()
print_book_publisher()
print_book_publisher()
print_book_publisher()
print_book_publisher()
'''
# case2
for _ in range(5) :
    print_book_publisher()
'''