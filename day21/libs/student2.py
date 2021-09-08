# 접근제한 - 맴버(private), 함수(public)
# 접근하는 방법 - get + 맴버이름(), set + 맴버이름()
class Student:
    def __init__(self, name):
        self._name = name
        self._grade = 0

    def learn(self):
        print("학생이 배웁니다.")

    def getname(self):
        return self._name

    def setgrade(self, grade):
        self._grade = grade

    def getgrade(self):
        return self._grade

    """
    def __str__(self):  # 객체의 정보 출력
        return "이름 : {0} {1}학년".format(self.name, self.grade)
    """

s1 = Student("흥부")
s1.setgrade(2)
print("이름 :", s1.getname())
print("학년 :", s1.getgrade())