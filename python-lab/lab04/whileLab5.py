while True :
    # 사용자로부터 문자열을 하나 입력받아 word라는 변수에 저장한다.
    word = input("단어를 입력하세요: ")
    # word 변수에 저장된 데이터의 길이를 추출하여 wordlength라는 변수에 저장한다.
    wordlength = len(word)

    # wordlength 라는 변수에 할당된 값에 따라서 다음 기능을 수행한다.
    # wordlength 라는 변수의 값이 0이면 반복을 종료한다.
    if wordlength == 0 :
        break
    # wordklength 라는 변수의 값이 5 이상이고 8 이하이면 아무 기능도 수행하지 않고 입력받는 기능부터 다시 수행한다
    elif 5 <= wordlength <= 8 :
         True # continue # pass
    # wordlength 라는 변수의 값이 5 미만이면 문자열의 앞과 뒤에 "*"기호를 붙여서 result 변수에 저장한다.
    elif wordlength < 5 :
        result = "*" + word + "*"
        print("유효한 입력 결과: ", result)
    # wordlength 라는 변수의 값이 8 초과이면 문자열의 앞과 뒤에 "$"기호를 붙여서 result 변수에 저장한다.
    else :
        result = "$" + word + "$"
        print("유효한 입력 결과: ", result)