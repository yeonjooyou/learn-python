import sys

sys.stdout = open('sample_yyyy_mm_dd.txt', 'a')

f1 = open("sample.txt", "rt", encoding="UTF-8")
text = ""
line = 1
while True:
    row = f1.readline() # 한 행씩 읽기
    if not row: break
    text += row
    line += 1
f1.close()
print(text)

sys.stdout.close()


# print("저장이 완료되었습니다.")