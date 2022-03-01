import sys
from collections import deque

n = int(sys.stdin.readline())
deque = deque()
for _ in range(n):
    cmd = list(sys.stdin.readline().split())

    if cmd[0] == 'push_front':
        deque.appendleft(cmd[1])
    elif cmd[0] == 'push_back':
        deque.append(cmd[1])
    elif cmd[0] == 'pop_front':
        print(deque.popleft() if deque else -1)
    elif cmd[0] == 'pop_back':
        print(deque.pop() if deque else -1)
    elif cmd[0] == 'size':
        print(len(deque))
    elif cmd[0] == 'empty':
        print(0 if deque else 1)
    elif cmd[0] == 'front':
        print(deque[0] if deque else -1)
    else:
        print(deque[-1] if deque else -1)