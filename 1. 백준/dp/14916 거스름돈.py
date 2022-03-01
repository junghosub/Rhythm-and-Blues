n = int(input())
coin = 0

while n >= 0:
    if n % 5 == 0: # 5의 배수라면
        coin += n // 5 # 5로 나눈 동전의 개수
        print(coin)
        break
    n -= 2 # 만약 5로 안 나눠진다면 2를 빼주는 것으로 5의 정수가 될 때까지 반복한다.
    coin += 1 # coin을 하나 더 추가함.
else:
    print(-1) # 만약 안 되면 -1 출력