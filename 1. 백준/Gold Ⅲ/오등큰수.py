# Ai가 수열 A에서 등장한 횟수를 F(Ai)라고 했을 때,
# Ai의 오등큰수는 오른쪽에 있으면서 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다.
# 그러한 수가 없는 경우에 오등큰수는 -1이다.

import sys

n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

ngf = [0 for _ in range(max(array)+1)]
for i in array: # 등장할 때마다 +1
    ngf[i] += 1

stk = [0]
answer = [-1] * n

for i in range(1, n):
    while stk and ngf[array[stk[-1]]] < ngf[array[i]]:
        answer[stk.pop()] = array[i]
    stk.append(i)
print(*(answer))
