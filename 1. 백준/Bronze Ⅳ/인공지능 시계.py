# 현재 시각인 h,m,s에서 t(단위:초)를 추가하여 오븐구이가 끝나는 시간을 출력
h, m, s = map(int, input().split())
t = int(input())

time = (h * 3600) + (m * 60) + (s + t);

print(time // 3600 % 24, time // 60 % 60, time % 60)