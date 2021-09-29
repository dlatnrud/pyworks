# group() - 매치된 문자열을 돌려준다.
# start() - 시작 위치
# end() - 끝 위치
# span() - (시작, 끝) 튜플 구조
import re

p = re.compile('[a-z]+')
m = p.match("hello")

print(m)
print(m.group())    # 문자열
print(m.start())    # 시작 위치 [0]
print(m.end())      # 끝 위치 [5]
print(m.span())     # (0, 5)튜플