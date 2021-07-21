while True :
    # 사용자로부터 월에 해당하는 숫자를 하나 입력 받는다.
    month = int(input("월을 입력하세요: "))

    # 입력된 숫자가 1~12 사이의 값이면
    if 1 <= month <= 12 :
        if month == 12 or 1 <= month <= 2 :
            print(month, "월은 겨울")
        elif 3 <= month <= 5 :
            print(month, "월은 봄")
        elif 6 <= month <= 8 :
            print(month, "월은 여름")
        else :
            print(month, "월은 가을")

    # 입력된 숫자가 1~12 사이가 아니면
    else :
        print("1~12 사이의 값을 입력하세요!")
        break