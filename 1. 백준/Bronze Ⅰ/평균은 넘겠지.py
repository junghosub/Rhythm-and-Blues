C = int(input())
count = 0

def who_over_mean(N, scores, count):
    for i in range(N):
        mean = (sum(scores) // N)
        if scores[i] > mean:
            count += 1
    print('{:.3f}'.format(count / N * 100)+ '%')
    # round 함수를 쓰면 40.0%로 나오므로 format 함수로 처리함

for i in range(1, C+1):
    scores = list(map(int, input().split()))
    N = scores[0]
    scores = scores[1:]
    who_over_mean(N, scores, count)

import numpy

c = int(input()) # 테스트의 개수 c
cnt= 0

for _ in range(c):
    scores = list(map(int, input().split()))
    n = scores[0] # 학생의 수 n
    scores = scores[1:] # n명의 점수
    mean_score = numpy.mean(scores)

    for i in range(n):
        if scores[i] > mean_score:
            cnt += 1
    print('{:.3f}'.format(cnt/n*100)+'%')