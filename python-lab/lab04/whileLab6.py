while True :
    # 숫자를 하나 입력받는다.
    inputNum = int(input("숫자 하나를 입력하세요 :"))

    # 입력된 숫자가 0이면 "종료"라는 메시지를 출력하고 수행을 종료한다.
    if inputNum == 0 :
        print("종료")
        break
    # 입력된 숫자가 -10 보다 작거나 10 보다 크면 입력 받는 것 부터 다시 시작한다.
    elif -10 > inputNum or inputNum > 10 :
        True # continue
    # 입력된 숫자가 양수이면
    elif inputNum > 0 :
        # "입력값: x"행을 출력한 다음
        print("입력값 :", inputNum)
        # 다음 행에 1부터 입력된 숫자 값까지의 곱한 결과를 출력한다.
        fac = 1
        while inputNum > 1 :
            fac *= inputNum
            inputNum -= 1
        print(fac)
    # 입력된 숫자가 음수이면
    else :
        # 양수로 변경하여 "입력값(부호변경) :x"를 출력한 다음
        inputNum = -inputNum
        print("입력값(부호변경) :", inputNum)
        # 다음 행에 1부터 입력된 숫자 값까지의 곱한 결과를 출력한다.
        fac = 1
        while inputNum > 1:
            fac *= inputNum
            inputNum -= 1
        print(fac)
