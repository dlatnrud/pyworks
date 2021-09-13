# 파일 읽기 - read() 함수 사용

f = open("c:/pyfile/file.txt", 'r')
data = f.read()    # 파일 내용을 읽어서 data에 저장
print(data)

f.close()

f = open("c:/pyfile/number2.txt", 'r')
data = f.read()    # 파일 내용을 읽어서 data에 저장
print(data)

f.close()