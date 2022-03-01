# 스네이크버드는 자신의 길이보다 작거나 같은 높이에 있는 과일들을 먹을 수 있습니다.
# 아이디어 : 자신이랑 작거나 같은 과일 다 먹음
fruit, snake = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

for i in h:
    if snake >= i:
        snake += 1
    else:
        break
print(snake)