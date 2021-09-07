import sys

stack = []
# push : value를 스택에 넣는 연산
def push(value):
    stack.append(value)

# pop : 맨 위에 있는 정수를 뺀다. 만약 스택에 들어간 정수가 없는 경우는 -1을 출력한다.
def pop():
    return -1 if len(stack) == 0 else stack.pop()

# size : 스택에 들어간 정수 개수를 출력한다.
def size():
    return len(stack)

# empty : 스택이 비어있으면 1, 아니면 0을 출력한다.
def empty():
    return 1 if stack else 0

# top : 스택 가장 위에 있는 수를 출력한다. 스택에 들어간 정수가 없다면 -1을 출력한다.
def top():
    return stack[-1] if stack else -1

n = int(sys.stdin.readline()) # 시간복잡도를 줄이기 위해 sys를 사용

for _ in range(n):
    order = sys.stdin.readline().rstrip().split() # 위와 동일
    if order[0] == 'push':
        push(order[1])
    elif order[0] == 'pop':
        print(pop())
    elif order[0] == 'size':
        print(size())
    elif order[0] == 'empty':
        print(empty())
    else:
        print(top())