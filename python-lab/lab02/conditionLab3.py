# 1. grade 라는 변수에 1부터 6사이의 숫자를 랜덤으로 추출하고 저장한다.
import random # 모듈
grade = random.randint(1, 6)
print(grade) #랜덤값을 확인하기 위한 출력문
# 조건 평가 시 and 연산자를 사용해서 해결한다.
if grade>=1 and grade <= 3:
    print(grade, "학년은 저학년입니다.")
else: # elif grade>=4 and grade<=6:
    print(grade, "학년은 고학년입니다.")