
from libs.myclass import Car, Student

s1 = Student("콩쥐", 3)
print(s1)
s1.learn()
s2 = Student("팥쥐", 2)
print(s2)

car1 = Car("소나타", "흰색", 2500)
car2 = Car("BMW", "black", 3000)

print("\t  모델명 \t색상 \t배기량")
print("차량1 " + car1.model + '\t' + car1.color + '\t' + str(car1.cc))
print("차량2 " + car2.model + '\t    ' + car2.color + '\t' + str(car2.cc))
