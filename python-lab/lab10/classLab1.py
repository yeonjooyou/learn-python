class Member:
    name, account, passwd, birthyear = None, None, None, None

    # 객체 초기화 메서드(생성자)
    def __init__(self, name, account, passwd, birthyear):
        # 인스턴스 변수 초기화
        self.name = name
        self.account = account
        self.passwd = passwd
        self.birthyear = birthyear

        # 회원 순번...
        print("회원 : {}({},{},{})".format(\
            self.name, self.account, self.passwd, self.birthyear))


# Member 클래스의 객체들 생성
Member("김민지", 'abc', '123', 1995)
Member("이가은", 'def', '456', 1996)
Member("박서현", 'ghi', '789', 1997)