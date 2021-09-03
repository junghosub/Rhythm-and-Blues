import collections

number = []

for i in range(10):
    i = int(input())
    number.append(i%42)

counter = collections.Counter(number)

sum = 0
for j in counter.keys():
    sum += list(counter).count(j)

print(sum)

# 숏코딩으로 하면 아래와 같다.
num = [int(input())%42 for i in range(10)]
print(len(set(num)))
# 집합은 중복이 없다는 성질을 이용했다.