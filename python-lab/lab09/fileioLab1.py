# c:/iotest/today.txt
import os
import calendar

def createFolder(directory):
    if not os.path.exists(directory):
            os.makedirs(directory)

createFolder('c:/iotest')

# =============== weekday  ===============
yoil = ['월', '화', '수', '목', '금', '토', '일']


f = open('c:/iotest/today.txt','w')

f.write("오늘은 2021년 07월 19일입니다.\n")
f.write("오늘은 "+yoil[calendar.weekday(2021,7,19)]+"요일입니다.\n")
f.write("나는 "+yoil[calendar.weekday(1999,10,21)]+"요일에 태어났습니다.\n")
# f.write("오늘은 %w요일 입니다." %(datetime.today().weekday()))

f.close()

print("저장이 완료되었습니다.")


