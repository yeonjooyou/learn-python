class Member:
    def __init__(self):
        self.name = None
        self.account = None
        self.passwd = None
        self.birthyear = None

member1 = Member()
member1.name = '철수'
member1.account = 'cjftn@naver.com'
member1.passwd = 'cjftn'
member1.birthyear = 1995

member2 = Member()
member2.name = '영희'
member2.account = 'dudgml@naver.com'
member2.passwd = 'dudgml'
member2.birthyear = 1996

member3 = Member()
member3.name = '민수'
member3.account = 'alstn@naver.com'
member3.passwd = 'alstn'
member3.birthyear = 1997

print("{}:{}({},{},{})".format('회원1', member1.name, member1.account, member1.passwd, member1.birthyear))
print("{}:{}({},{},{})".format('회원2', member2.name, member2.account, member2.passwd, member2.birthyear))
print("{}:{}({},{},{})".format('회원3', member3.name, member3.account, member3.passwd, member3.birthyear))