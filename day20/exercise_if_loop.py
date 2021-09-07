# exercise - 제어문 (146p)
# 1
a = "Life is too short, you need python"

if "wife" in a:
    print("wife")
elif "python" in a and "you" not in a:
    print("python")
elif "shirt" not in a:  # 출력하고 if문 종료
    print("shirt")
elif "need" in a:
    print("need")
else:
    print("none")

# 2
result = 0      # 합
i = 1
while i <= 1000:
    if i % 3 == 0:      # 3으로 나누어 떨어지는 수는 3의 배수
        result += i     # 누적 합
    i += 1

print(result)       # 166833 출력

# 3
i = 0
while True:
    i += 1          # while문을 수행할 때 1씩 증가
    if i > 5:       # i 값이 5를 초과하면 while문을 벗어난다.
        break       
    print(i * '*')  # i 값 개수만큼 '*'을 출력

print()

for i in range(0, 5):
    for j in range(0, i+1):     # j의 종료값 변경
        
        print("*", end='')
    print()

# 4
for i in range(1, 101):
    print(i)
