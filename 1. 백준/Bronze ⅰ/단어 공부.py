import collections
word = str(input())
word = word.lower()

lst = (collections.Counter(word).most_common())

for i in range(len(lst)):
    if len(lst) == 1:
        print(lst[0][0].upper())
    else:
        if lst[0][1] != lst[1][1]:
            print(lst[0][0].upper())
            break
        else:
            print('?')
            break
