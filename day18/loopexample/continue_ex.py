# 반복문 : continue문
# 1 ~ 10 중 5만 제외하고 출력
# 반복하다가 조건에 맞으면 수행문을 처리하지 않고 다시 반복
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

print()
    
# 1 ~ 10 중 짝수만 출력
for i in range(1, 11):
    if i % 2 == 1:
        continue
    print(i)
