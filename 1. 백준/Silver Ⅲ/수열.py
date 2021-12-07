import sys

def dp(array, n):
    dp1,dp2 = [1]*n, [1]*n
    for i in range(1, n):
        if array[i] <= array[i-1]: # 내림차순
            dp1[i] = max(dp1[i], dp1[i-1]+1)
        if array[i] >= array[i-1]: # 오름차순
            dp2[i] = max(dp2[i], dp2[i-1]+1)
    return max(max(dp1), max(dp2))

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
print(dp(array,n))