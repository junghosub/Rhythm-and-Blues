while True:
    tri = list(map(int, input().split()))
    tri = sorted([tri[i] ** 2 for i in range(3)])
    if tri == [0,0,0]:
        break
    print('right' if tri[2] == tri[0] + tri[1] else 'wrong')