# 현재 시간인 h,m에 t분을 추가한 시간을 출력한다. 다만 24시가 넘어가면 0시로 출력한다.
h, m = map(int, input().split())
t = int(input())
print((h+(m+t)//60) % 24, (m+t) % 60)