# evenNum 변수와 oddNum 변수의 값을 0으로 대입한다.
e, evenNum = 0, 0
o, oddNum  = 0, 0

# 1 부터 100 까지의 값 중에서
# 짝수의 합은 evenNum 에 누적하고
# 홀수의 합은 oddNum 에 누적한다.
'''
for e in range(2, 102, 2):
    evenNum += e
for o in range(1, 101, 2):
    oddNum += o
'''

for i in range(1,101) :
    if i % 2 == 0 :
        evenNum += i
    else :
        oddNum += i

print("1부터 100까지의 숫자들 중에서")
print("짝수의 합은 ", evenNum, " 이고")
print("홀수의 합은 ", oddNum, " 이다.")

# print("1부터 100까지의 숫자들 중에서 \n짝수의 합은", evenNum," 이고 \n홀수의 합은", oddNum, "이다.")