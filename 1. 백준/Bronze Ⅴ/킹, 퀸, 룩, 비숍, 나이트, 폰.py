right_answer = [1, 1, 2, 2, 2, 8]

white = map(int, input().split())
white = list(white)

answer = [i - j for i, j in zip(right_answer, white)]

for i in answer:
    print(i, end = ' ')
# 컴프리헨션과 zip을 통해 연산 가능하다.