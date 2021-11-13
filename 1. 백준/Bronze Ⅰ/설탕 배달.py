# 배달해야할 N 킬로그램
sugar = int(input())
bag = 0
while sugar >= 0:
    if sugar % 5 == 0: # 설탕이 5의 배수이면
        bag += (sugar // 5) # 5를 나눈 몫을 구해야 정수
        print(bag)
        break
    sugar -= 3
    bag += 1
else:
    print(-1)

# 해답 봤음.