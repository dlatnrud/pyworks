# 학생 5명의 개인별 국어, 수학 점수 계산

score = [
    {'name': '이대한', 'korean': 90, 'math': 70},
    {'name': '장민국', 'korean': 85, 'math': 76},
    {'name': '오상식', 'korean': 80, 'math': 65},
    {'name': '천선란', 'korean': 95, 'math': 85},
    {'name': '김초엽', 'korean': 85, 'math': 70}
]
print('이름   총점 평균')
for s in score:
    sum_v = s['korean'] + s['math']
    avg = sum_v / 2
    print(s['name'], sum_v, avg)

print()

# 과목별 국어, 수학 점수 계산
sum_kor = 0
sum_math = 0

for s in score:
    sum_kor += s['korean']
    sum_math += s['math']

avg_kor = sum_kor / len(score)
avg_math = sum_math / len(score)
print("국어 합계 : %d점" % sum_kor)
print("수학 합계 : %d점" % sum_math)
print("국어 평균 : %.1f점" % avg_kor)
print("수학 평균 : %.1f점" % avg_math)