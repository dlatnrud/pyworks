# 2차원 리스트 - 문자열(1차원), 숫자와 함께 사용
e = [7, 3, ['chicken', 'cow', 'pig', 'horse']]

# chicken에 접근
print(e[0])         # 7
print(e[1])         # 3
print(e[2])         # ['chicken', 'cow', 'pig']
print(e[2][0])      # chicken

print(e[2][2])      # pig에 접근
print(e[2][-1])     # horse

# 슬라이싱
print(e[2][1:])
print(e[2][:3])
