# 5부터 10 사이의 난수를 추출한다.
import random
square = random.randint(5, 10)
# print("랜덤값 :", square)

# 1부터 추출된 숫자값까지의 각 숫자들의 제곱값을 행단위로 출력한다.
i = 1
while i < square+1 :
    print(i, "->", i ** 2)  # 제곱연산자: **
    i += 1

'''
# case 2
import random
end_num = random.randint(5,10)
now_num = 1

while now_num <= end_num:
    print(now_num, '->', now_num**2)
    now_num += 1
'''