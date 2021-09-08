
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):  # 더하기(add)
        return self.x + self.y

    def sub(self):  # 빼기(sub)
        return self.x - self.y

    def mul(self):  # 곱하기(mul)
        return self.x * self.y

    def div(self):  # 나누기(div)
        if self.y == 0:
            print("0으로 나눌 수 없습니다.")
            return 0
        else:
            return self.x / self.y

cal = Calculator(5, 0)
print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())