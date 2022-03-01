import sys
from collections import deque

n, k = list(map(int, sys.stdin.readline().split()))
circle = [i for i in range(1, n+1)]

front = 0
answer = deque()

for _ in range(n):
    front += k-1
    if front >= len(circle):
        front = front % len(circle)
    answer.append(str(circle.pop(front)))
print('<', ', '.join(answer)[:],'>', sep = '')