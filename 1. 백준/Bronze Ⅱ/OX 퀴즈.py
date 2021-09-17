N = int(input())

for _ in range(N):
    test = list(input())

    score = 0 # 초기 스코어 지정
    temp = 1 # 증가하는 값
    for i in test:
        if i == 'O':
            score += temp
            temp += 1
        else:
            temp = 1 # 만약 X가 나오면 temp는 다시 1로 초기화
    print(score)

# 이건 해답을 봤음.