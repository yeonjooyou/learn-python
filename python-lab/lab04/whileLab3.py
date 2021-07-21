import random
i = 0
while True :
    # 0부터 30사이의 난수를 추출한다.
    num = random.randint(0, 30)
    # print("랜덤값 :", num)

    # 난수가 0이 추출되거나 27~30이 추출되면 반복을 끝낸다.
    if num == 0 or 27 <= num <= 30 :
        break
    else :
        #추출된 숫자가 1이면 'A',...를 출력한다.
        # ASCII 코드를 이용하여 추출된 숫자를 알파벳으로 바꾸는 과정
        order = num + 64
        string = chr(order)
        print(string, '(', num, ')', sep='')
        i += 1   # 수행횟수를 저장하는 변수 i
print("수행횟수는 ", i, "번 입니다.")

'''
# case 2
import random
count = 0     # 데이터 값의 용도에 따라 변수명을 사용하기
while True :
    num = random.randint(0,30)
    if 1 <= num <= 26 :
        print(chr(num+64), "(", num, ")", sep="")
        count += 1
        # continue는 사용하지 않아도 됨_deadcode
    elif num == 0 or num > 26 :
        print('수행횟수는', count, '번 입니다.')
        break
'''