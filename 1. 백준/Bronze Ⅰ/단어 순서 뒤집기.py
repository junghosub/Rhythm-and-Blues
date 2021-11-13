n = int(input())
stack = []

for i in range(n):
    word = list(input().split())
    stack = word[::-1] # 스택의 push와 같은 느낌
    print('Case #{0}:'.format(i+1),*(stack))