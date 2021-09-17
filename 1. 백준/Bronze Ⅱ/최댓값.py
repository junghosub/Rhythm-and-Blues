lst = []

for i in range(9):
    i = int(input())
    lst.append(i)
print(max(lst),lst.index(max(lst)) + 1)
