import bisect
import sys

def solution(a,b):
    cnt = 0
    for key in a:
        cnt += bisect.bisect_left(b, key)
    return cnt

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    a.sort()
    b.sort()
    print(solution(a,b))