time = []
# 입력
for i in range(4):
    i = int(input())
    time.append(i)

sum = 0
# 더하기
for j in time:
    sum += j

print(sum // 60)
print(sum % 60)
