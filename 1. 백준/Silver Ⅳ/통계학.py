import collections

n = int(input())
lst = []

for _ in range(n):
    num = int(input())
    lst.append(num)

# 정렬
lst.sort()
mean = round(sum(lst) / len(lst),0)
print('%.0f' % mean)

median = lst[len(lst)//2]
print(median)

if len(lst) > 1:
    mode = collections.Counter(lst).most_common(2)
    print(mode[0][0] if mode[0][1] > mode[1][1] else mode[1][0])
else:
    mode = collections.Counter(lst).most_common(1)
    print(mode[0][0])

range = max(lst) - min(lst)
print(range)
