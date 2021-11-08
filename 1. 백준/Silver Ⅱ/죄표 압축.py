import sys
import bisect

def bisect_count(array, x):
    return bisect.bisect_right(array,x) -bisect.bisect_left(array,x)

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

for i in array:
