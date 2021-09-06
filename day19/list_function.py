# 리스트 함수 사용하기

num = []    # 빈 num 리스트 선언

print("요소(값) 추가 - append(), insert()")
num.append(90)      # 맨 뒤 추가
num.append(80)
num.insert(1, 50)   # 1번 인덱스에 50을 추가
num.append(70)
num.append(60)
num.append(100)
print(num)

print("요소(값) 삭제 - pop(), remove()")
num.pop()       # 맨 뒤 삭제
num.remove(80)  # 특정 요소 삭제
print(num)

print("정렬 - sort() : 오름차순, reverse() : 거꾸로 뒤집기")
num.reverse()
print(num)
num.sort()
print(num)
