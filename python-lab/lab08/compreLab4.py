# 실습 9
import random

random_list = []
while True :
    random_list.append(random.randint(0, 100))
    if len(random_list) == 10 :
        break
print(random_list)

# 딕셔너리 생성
dict = {str(i) : 'pass' if random_list[i-1] >= 60 else 'nopass' for i in range(1, 11)}
print(dict)


# case 2
nums = [random.randint(1, 100) for _ in range(10)]
print(nums)

check_pass = {i+1 : 'pass' if nums[i] >= 60 else 'nopass' for i in range(10)}
print(check_pass)