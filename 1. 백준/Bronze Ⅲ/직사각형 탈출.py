x, y, w, h = map(int, input().split())

# x의 최솟값
if x > w/2:
    min_x = w - x
else:
    min_x = x

# y의 최솟값
if y > h/2:
    min_y = h - y
else:
    min_y = y

print(min_x if min_x <= min_y else min_y)

# 숏코딩
print(min(x,y,h-y,w-x))