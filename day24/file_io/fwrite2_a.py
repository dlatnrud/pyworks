# a모드는 주로 input() 코드에서 필수 사용
# 연산은 문자열 포메팅 방식으로 가능함
f = open("c:/pyfile/number2.txt", 'a')
f.write("%d\n" % (100+2))
f.write("%.2f\n" % (3.14*5*5))  # 원의 넓이 괄호()에 포함해야 함
num = "%d\n" % 150000   # 변수로 저장
f.write(num)
f.write("%d\n" % 7)
f.close()