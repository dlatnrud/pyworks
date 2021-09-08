# 도형 그리기
# 변수 사용하기
import turtle as t

t.shape("turtle")

# 사각형
n = 4
d = 150
t.pensize(2)
for i in range(n):
    t.forward(d)
    t.right(360/n)

# 삼각형
n = 3
t.color("blue")
t.pensize(3)
for i in range(n):
    t.forward(d)
    t.left(360/n)

# 원
t.color("red")
t.circle(100)    # 반지름이 100px

t.mainloop()