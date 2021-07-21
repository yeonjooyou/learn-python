import random
start = random.randint(1, 10)
end = random.randint(30, 40)
print("시작 값 :", start, ", 끝 값", end)

evenSum = 0
for i in range(start, end+1, 1):
    if i % 2 == 0 :
        evenSum += i
print(start, '부터', end, '까지의 짝수의 합: ', evenSum)

'''
s = start
e = end
sum = 0 # 짝수들의 합

# 시작 값이 짝수
if(s % 2 == 0) :
    # 끝 값이 짝수
    if(e % 2 == 0):
        for s in range(s, e+1, 2) :
            sum += s
            s += 2
    # 끝 값이 홀수
    else :
        for s in range(s, e, 2) :
            sum += s
            s += 2
# 시작 값이 홀수
elif(s % 2 == 1) :
    # 끝 값이 짝수
    if(e % 2 == 0) :
        for add in range(s+1, e+1, 2) :
            sum += add
            s += 2
    # 끝 값이 홀수
    else :
        for add in range(s+1, e, 2) :
            sum += add
            s += 2
'''
# print(start, "부터", end, "까지의 짝수의 합:", sum)