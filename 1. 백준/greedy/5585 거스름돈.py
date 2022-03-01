# 물건의 가격
price = 1000 - int(input())
# 잔돈의 종류
array = [500,100,50,10,5,1]
count = 0

for yen in array:
    count += price // yen
    price %= yen
print(count)
