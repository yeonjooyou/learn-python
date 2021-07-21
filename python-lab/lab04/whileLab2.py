import random

while True :
    # 1부터 6사이의 두 개 난수를 추출하여 각각 pairNum1, pairNum2에 저장한다.
    pairNum1 = random.randint(1, 6)
    pairNum2 = random.randint(1, 6)

    print("pairNum1 :", pairNum1, "pairNum2 :", pairNum2)

    # 추출된 두 개의 숫자가 서로 다르면 값의 크기를 비교한다.
    if pairNum1 > pairNum2 :
        print("pairNum1이 pairNum2 보다 크다.")
        continue
    elif pairNum1 < pairNum2 :
        print("pairNum1이 pairNum2 보다 작다.")
        continue
    # 추출된 두 개의 숫자가 동일하면 종료한다.
    else :
        print("게임 끝")
        break