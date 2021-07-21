import random
score = random.randint(0, 100)
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
# 한 개의 print() 함수로 해결한다.
print(score, "점은", grade, "등급입니다.")