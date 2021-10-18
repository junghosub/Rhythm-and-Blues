# 점수가 40점 미만이면 40점이고, 40점 이상이면 본인 점수 그대로 받는다.
# 5명의 평균 점수를 출력
scores = []

for _ in range(5):
    score = int(input())
    if score < 40:
        scores.append(40)
    else:
        scores.append(score)
print(round(sum(scores) / 5))