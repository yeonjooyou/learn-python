# 실습 1
# 가변 키워드 인수
def mydict(**str) :
    dict = {}
    if not str :
        return dict
    else :
        for _ in str :
            dict = {"my" + k : v for k, v in str.items()}
        return dict

print(mydict())
print(mydict(나이=18))
print(mydict(나이=18, 키=160, 몸무게=60))

print('-'*40)

# case 2
def mydict2(**kargs) :
    mykargs = {}
    for k, v in kargs.items() :
        mykargs['my'+k] = v
    return mykargs

print(mydict2(a=2, b=3))
print(mydict2(a=2))
print(mydict())