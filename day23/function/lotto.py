
import random as r

# 로또번호 생성기(1 ~ 45) - 6개
lotto = []

# 중복되는 수 없이 6개에 랜덤 수 출력하기
while len(lotto) < 6:       # len(lotto) : 0 ~ 5
    rnd = r.randint(1, 45)  # 랜덤 수
    if rnd not in lotto:    # rnd(난수)가 lotto 리스크에 없을 때
        lotto.append(rnd)   # rnd 추가

"""
# 개수가 6개가 안됨
for i in range(6):
    rnd = r.randint(1, 45)  # 랜덤 수
    if rnd not in lotto:    # rnd(난수)가 lotto 리스트에 없을때
        lotto.append(rnd)   # rnd 추가
"""

print(lotto)