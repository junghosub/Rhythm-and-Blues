# 가능한 선택지를 모두 만든 후, 스트라이크와 볼을 비교하여 같지 않으면 가능한 선택지에서 삭제.
import itertools
import sys

# 선택지 생성
nums = list(map(list, itertools.permutations([str(i) for i in range(1,10)], 3)))
stk = []
n = int(sys.stdin.readline())
# 입력 받음
for _ in range(n):
    array, strike, ball = map(int, sys.stdin.readline().split())
    array = list(str(array))

    for num in nums:
        s, b = 0, 0
        for i in range(3):
            if array[i] in set(num):
                if array[i] == num[i]:
                    s += 1
                else:
                    b += 1
        if strike != s or ball != b:
            stk.append(num)
    while stk:
        nums.remove(stk.pop())
print(len(nums))