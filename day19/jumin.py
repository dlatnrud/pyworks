# 3
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd) # 연월일 부분 출력
print(num)      # 숫자 부분 출력

# 4 성별 문자가 1이면 '남자', 아니면 '여자'
print(pin[7])
if pin[7] == "1" or pin[7] == "3":
    print("남자")
else:
    print("여자")

# 5
a = "a:b:c:d"
b = a.replace(":", "#")
print(b)    # 문자열 "a#b#c#d" 출력

# 6
a = [1, 3, 5, 4, 2]
a.sort()        # [1, 2, 3, 4, 5]로 변경
a.reverse()     # [5, 4, 3, 2, 1]로 변경
print(a)

# 7 리스트 -> 문자열
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)   # "Life is too short" 출력
