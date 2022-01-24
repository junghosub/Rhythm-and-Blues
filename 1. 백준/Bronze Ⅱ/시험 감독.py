n = int(input())
array = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = n # 모든 시험장엔 1명의 총감독관이 들어가야하니까 바로 더해줌.

for num in array:
    num -= b # 총감독관이 감시할 수 있는 수를 제외해줌.
    if num > 0: # 부감독관이 필요하다면
        cnt += num //c # 몫 연산을 통해 감독관의 수를 더해줌
        num %= c # 이제 남은 응시자 수는 나머지
        if num != 0: # 부감독관을 한 명 더 추가해서 모든 응시자를 감시함.
            cnt += 1
print(cnt)