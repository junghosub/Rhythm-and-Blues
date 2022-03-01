import sys
from itertools import combinations

dwarf = [int(sys.stdin.readline()) for _ in range(9)]

for i in list(combinations(dwarf, 7)):
    if sum(i) == 100:
        print(*(sorted(i)), sep = '\n')
        break