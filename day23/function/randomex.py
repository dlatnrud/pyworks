
import random
import math

# 0.0 <= r < 1.0
print(random.random())

# random.randint(1, 10) - 1부터 10까지 무작위수
rand1 = random.randint(1, 10)
rand2 = math.floor(random.random() * 10) + 1
print(rand1)
print(rand2)

# 문자 추출 - random.choice()
fruit = ['포도', '딸기', '사과']
rnd = math.floor(random.random() * len(fruit))    # 0 ~ 2
# print(rnd)
# print(fruit[rnd])
print(random.choice(fruit))