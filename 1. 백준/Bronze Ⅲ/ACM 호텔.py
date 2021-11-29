import sys

t = int(sys.stdin.readline())
for _ in range(t):
    room = []
    h, w, n = map(int, sys.stdin.readline().split())
    for no in range(1, w+1):
        for floor in range(1, h+1):
            if no < 10:
                room.append(str(floor)+'0'+str(no))
            else:
                room.append(str(floor)+str(no))
    print(room[n-1])