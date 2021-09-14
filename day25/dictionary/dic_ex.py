# 딕셔너리 예제

dic = {1: 'A', 2: 'B', 3: 'C'}

dic[4] = 'D'
print(dic)

# 수정
dic[4] = 'E'
print(dic)

# 삭제
dic.pop(2)  # key를 선언
print(dic)

# dic 요소 출력
for key in dic:
    print(key)
    print(dic[key]) # key, value 모두 출력
