import sys

stk1 = list(sys.stdin.readline().strip())
stk2 = []
n = int(sys.stdin.readline())

for _ in range(n): # 명령어 입력
    command = sys.stdin.readline().split()
    if command[0] == 'L' and stk1:
        stk2.append(stk1.pop())
    elif command[0] == 'D' and stk2:
        stk1.append(stk2.pop())
    elif command[0] == 'B' and stk1:
        stk1.pop()
    elif command[0] == 'P':
        stk1.append(command[1])
print(*stk1+list(reversed(stk2)), sep = '')

