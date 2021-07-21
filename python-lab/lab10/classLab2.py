class Book:
    count = 0 # 카운트 순번...
    books = []

    @classmethod
    def print(cls):
        for book in cls.books:
            print(Book.str(book))
            print(Book.getBookInfo(book))
            print('-'*40)

    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        Book.count += 1
        Book.books.append(self)

    def getBookInfo(self):
        return "책이름 : {} \n 저자 : {} \n 가격 : {}".format(\
            self.title,\
            self.author,\
            self.price)

    def str(self):
        return "[ 객체 {} : Book 클래스로 생성된 객체 ]".format(self.count)

# Book 클래스의 객체 5개 생성
Book("파이썬 정복", "김상형", 22000)
Book("이것이 MariaDB다", "우재남", 30000)
Book("맛있는 MongoDB", "정승호", 28000)
Book("점프 투 장고", "박응용", 19800)
Book("생활코딩!", "이고잉", 27000)

Book.print()