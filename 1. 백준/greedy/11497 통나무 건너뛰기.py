import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    l = list(map(int,sys.stdin.readline().split()))
    l.sort()
    res = 0
    for j in range(2, n):
       res = max(res, abs(l[j]-l[j-2]))
    print(res)

# 혹은 이런 방법
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    l = list(map(int,sys.stdin.readline().split()))
    l.sort()
    max = 0
    for idx in range(len(l)-1, 1, -1):
        if  max < l[idx] - l[idx-2]:
            max = l[idx] - l[idx-2]
    print(max)
