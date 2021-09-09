# 제곱수 구하는 함수 정의
import math


def square(x):
    return x * x


# 거듭제곱을 계산하는 함수
def double_times(x, y):
    return x ** y


# 절대값 구하는 함수1
def abs_v(x):
    if x < 0:
        return -x
    else:
        return x


# 절대값 구하는 함수2
def abs_v2(x):
    y = x * x
    return math.sqrt(y)


# 호출
n = square(5)
n2 = double_times(2, 5)     # sqrt() 제곱근 함수

# 출력
print("제곱수 :", n)
print("거듭제곱 :", n2)
print("절대값 :", abs_v(-10))
print("절대값 :", abs_v2(-10))