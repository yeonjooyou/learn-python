# 실습 4
def mycompredict(**str) :
    dict = {}
    if not str :
        return dict
    else :
        for _ in str:
            dict = {"my" + k: v for k, v in str.items()}
            # dict.update(str)
        return dict

# case 2
def mycompredict2(**str) :
    dict = {"my" + k: v for k, v in str.items()}

print(mycompredict())
print(mycompredict(나이=18))
print(mycompredict(나이=18, 키=160, 몸무게=60))