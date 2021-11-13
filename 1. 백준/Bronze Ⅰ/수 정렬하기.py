N = int(input())
lst = []

for i in range(N):
    a = int(input())
    lst.append(a)
lst.sort()

print(*(set(lst)), sep = '\n')

n = int(input())
numbers = []

for _ in range(n):
    number = int(input())
    numbers.append(number)
numbers.sort()
print(*numbers, sep = '\n')