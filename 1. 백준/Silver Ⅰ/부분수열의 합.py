import sys
from itertools import combinations

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))

array = set()
for i in range(1, n+1):
    for j in list(map(sum, combinations(s,i))):
        array.add(j)

i = 1
while True:
    if i not in array:
        print(i)
        break
    i += 1