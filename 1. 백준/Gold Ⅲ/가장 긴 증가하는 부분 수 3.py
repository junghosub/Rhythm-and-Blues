# time complexity O(nlogn) using binary search
# LIS의 마지막 원소가 가능한 작을수록 더 긴 LIS를 생성할 수 있다.
import sys

# 이분 탐색 구현
def bisect(key, array):
    pl = 0
    pr = len(array) - 1
    while pl <= pr:
        pc = (pl+pr) // 2

        if key == array[pc]:
            return pc
        elif key > array[pc]:
            pl = pc + 1
        else:
            pr = pc - 1
    return pl

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = []

for num in arr:
    if len(dp) == 0 or num > dp[-1]:
        dp.append(num)
    if num < dp[-1]:
        idx = bisect(num, dp)
        dp[idx] = num
print(len(dp))

# list는 인덱스 접근이 O(1)이고, deque은 인덱스 접근이 O(N) 걸린다.