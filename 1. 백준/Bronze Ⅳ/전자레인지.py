# 최소버튼 조작을 해야하므로 A버튼부터 누른다.
buttons = [300, 60, 10]
t = int(input())

# 버튼은 초 단위가 없으므로 10으로 나누어 떨어지지 않으면 -1이다.
for button in buttons:
    if t % 10 == 0:
        cnt = 0
    cnt = t // button  # 몫을 이용하여 누른 횟수를 구함.
    t %= button # 버튼을 누르고 남은 시간을 나머지로 구해줌.
    print(cnt, end = ' ')
else:
    print(-1)