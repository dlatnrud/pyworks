
# 1
def is_odd(number):
    if number % 2 == 1:     # 2로 나누었을 때 나머지가 1이면 홀수이다.
        return True
    else:
        return False

n1 = is_odd(10)
print(n1)
print(is_odd(11))


# 2
def avg_numbers(*args):
    result = 0      # 합계
    for i in args:
        result += i
    return result / len(args)   # 평균 = 합계 / 개수

print(avg_numbers(1, 2))        # 1.5 출력
print(avg_numbers(1,2,3,4,5))   # 3.0 출력

"""
# 3
input1 = input("첫번째 숫자를 입력하세요 : ")
x = int(input1)
input2 = input("두번째 숫자를 입력하세요 : ")
y = int(input2)

total = x + y
# total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)
"""

# 4
print("you""need""python")
print("you"+"need"+"python")
print("you","need","python")
print("".join(["you","need","python"]))
# join() : 리스트의 요소를 문자열로 바꿈


# 5
"""
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()
"""

with open("test.txt", 'w') as f1:
    f1.write("Life is too short")

with open("test.txt", 'r') as f2:
    print(f2.read())


# 6
user_input = input("저장할 내용을 입력하세요 : ")
f = open("test2.txt", 'a')       # 내용을 추가하기 위해 'a'를 사용
f.write(user_input)
f.write('\n')       # 입력한 내용을 줄 단위로 구분하기 위해 줄 바꿈 문자 삽입
f.close()