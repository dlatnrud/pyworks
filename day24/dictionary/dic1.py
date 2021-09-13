# 딕셔너리(dictionary) 자료구조
# 키(key)와 값(value)으로 이루어짐

person = {}    # 빈 딕셔너리 선언
person['name'] = '장그래'
person['age'] = 29
person['phone'] = '010-2424-3535'
person['gender'] = '남자'
print(person)

del person['age']    # age 요소 삭제
print(person)

person['name'] = '오상식'    # 수정
print(person)