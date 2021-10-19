import sys

t = int(sys.stdin.readline())

for _ in range(t):
    l = sys.stdin.readline().rstrip()
    stk1 = []
    stk2 = []

    for command in l:
        if command == '<' and stk1:
            stk2.append(stk1.pop())
        elif command == '>' and stk2:
            stk1.append(stk2.pop())
        elif command == '-'  and stk1:
            stk1.pop()
        elif command.isalnum():
            stk1.append(command)
    result = stk1+list(reversed(stk2))
    print(''.join(result))