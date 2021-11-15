import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(1, n+1):
    answer = list(map(sum, combinations(array, i)))
    cnt += answer.count(s)
print(cnt)