# 실습 2
def myprint(*arg, deco="**", sep=',') :
    if not arg :
        print("Hello Python")
    else :
        print(deco, end='')
        for data in arg :
            print(data, sep, end='')
        print(deco)

myprint(10, 20, 30, deco="@", sep="-")
myprint("python", "javascript", "R", deco="$")
myprint("가", "나", "다")
myprint(100)
myprint(True, 111, False, "abc", deco="&", sep="")
myprint()