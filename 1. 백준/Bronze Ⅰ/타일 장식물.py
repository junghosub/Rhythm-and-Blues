import sys

def solution(n):
    array = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        array[i] = array[i-1] + array[i-2]
    circum = 2*array[-1] + 2*array[-2]
    return circum

n = int(sys.stdin.readline())
print(solution(n))
