# 이름과 전화번호를 분리해서 추출하기
# sub(\g<그룹이름>)

import re
str = "jang 010-1324-5678"
# p = re.compile("(\w+)\s(\d+[-]\d+[-]\d+)")   # [0-9A-Za-z]+와 같은 형식 - \w+
p = re.compile("(?P<name>\w+)\s(?P<phone>[0-9]+[-]\d{4}[-][0-9]{4})")
# s = p.sub("\g<name> \g<phone>", str)
s = p.sub("\g<1> \g<2>", str)
print(s)
