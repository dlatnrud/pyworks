# 예외 만들기 - 사용자가 직접 만들기
# 내장 Exception 클래스를 상속하여 만든다

class MyError(Exception):   # 문자로 리턴해줌
    # pass
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()   # Error를 발생 시킴(미뤄놓음)
    print(nick)

# Error를 사용하는 곳에서 try~except 처리해야 함
try:
    say_nick('Hero')
    say_nick('angel')
    say_nick("바보")
except MyError as e:    # e : exception의 줄임말
    # print("허용되지 않는 별명입니다.")
    print(e)