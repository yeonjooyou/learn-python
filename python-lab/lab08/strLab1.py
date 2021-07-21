# 실습 5
def myemail_info(email) :
    # 전달된 문자열에 @가 없으면 None을 리턴한다.
    if not '@' in email :
        return None
    else :
        # 전달된 이메일 주소 문자열에서 @를 기준으로 쪼개서 튜플을 만들어 리턴한다.
        tu = tuple(email.split('@'))
        return tu

print(myemail_info("admin@naver.com"))
print(myemail_info("admin.com"))
