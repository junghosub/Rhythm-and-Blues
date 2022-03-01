duck = []
ptr = 0
while duck  != '고무오리 디버깅 끝':
    duck = input()

    if duck == '문제':
        ptr += 1
    elif duck == '고무오리':
        if ptr <= 0:
            ptr += 2
        else:
            ptr -= 1
print('고무오리야 사랑해' if ptr == 0 else '힝구')