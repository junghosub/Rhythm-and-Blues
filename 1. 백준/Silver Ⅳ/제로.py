k = int(input())
stack = []

def pop():
    if len(stack) != 0:
        stack.pop()

for _ in range(k):
    num = int(input())

    if num == 0:
        pop()
    else:
        stack.append(num)
print(sum(stack))