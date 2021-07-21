# 실습 7
listv1 = ["A", "b", "c", "D", "e", "F", "G", "h"]
listv2 = [d for d in listv1 if 97 <= ord(d) <= 122]
print(listv2)