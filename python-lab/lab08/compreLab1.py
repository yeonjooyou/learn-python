# 실습 3
def createList(type = 1, *point) :
    list = []
    if len(point) == 0 :
        point = [p for p in range(1, 31)]
    elif type == 2 :
        list = [p for p in point if p % 2 == 0]
    elif type == 3 :
        list = [p for p in point if p % 2 != 0]
    elif type == 4 :
        list = [p for p in point if p > 10]
    elif type == 1 :
        list = [p for p in point]
    return list

print(createList())
print(createList(1, 3, 4, 5, 10, 11))
print(createList(2, 3, 4, 5, 10, 11))
print(createList(3, 3, 4, 5, 10, 11))
print(createList(4, 3, 4, 5, 10, 11))
