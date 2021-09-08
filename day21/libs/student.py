
class Student:
    def __init__(self):
        print("객체를 생성합니다.")
        self.name = "콩쥐"
        self.grade = 2

s1 = Student()
print(s1.name, s1.grade)