class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def intro(self):
        print(str(self.age) + "살 " + self.name + "입니다")

    def eat(self):
        print("밥을 먹는다")


class Student(Human): # class 자식클래스(부모클래스)
    def __init__(self, age, name, stunum):
        super().__init__(age, name)
        self.stunum = stunum

    def intro(self): # 메서드 오버라이딩
        super().intro()
        print("학번 : " + str(self.stunum))

    def study(self): # 추가
        print("하늘천 따지 검을현 누를황")


kim = Human(29, "김상형")
kim.intro()
kim.eat()
print("-*-"*10)
lee = Student(34, "이승우", 930011)
lee.intro()
lee.study()
lee.eat()
