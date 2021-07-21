# 1. score 라는 변수에 0부터 100 사이의 숫자를 랜덤으로 추출하고 저장한다.
import random
score = random.randint(0, 100)
# score 변수의 값의 크기에 따라서 다음의 내용을 출력한다.
# print() 함수를 5개 사용하여 해결한다.
if score >= 90:
    print(score, "점은 A등급입니다.")
elif score >= 80:
    print(score, "점은 B등급입니다.")
elif score >= 70:
    print(score, "점은 C등급입니다.")
elif score >= 60:
    print(score, "점은 D등급입니다.")
else:
    print(score, "점은 F등급입니다.")