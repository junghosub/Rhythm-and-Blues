N = int(input())

for i in range(5):
    if N < 10:
        lst = list(str(N))
        lst.insert(0, '0')
    else:
        lst = list(str(N))
        lst.append(int(lst[i]) + int(lst[i+1]))
