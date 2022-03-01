import sys
expression = sys.stdin.readline().rstrip() # 중위 표기식 입력 받음
answer = [] # 리스트
stack = [] # 스택
operand = {'+':1,'-':1,'*':2,'/':2, '(':0}

for token in expression:
    if token.isalpha(): # 만약 피연산자라면 리스트에 추가
        answer.append(token)
    elif token == '(': # 우선순위가 높은 연산자는 모두 pop()하고 자신이 push 됨.
        stack.append(token)
    elif token == ')':
        while stack and stack[-1] != '(':
            answer.append(stack.pop())
        stack.pop()
    else:
        while stack and operand[token] <= operand[stack[-1]]:
            answer.append(stack.pop())
        stack.append(token)

while stack: # stack에 남은 연산자 모두 pop()
    answer.append(stack.pop())
print(*(answer), sep='')