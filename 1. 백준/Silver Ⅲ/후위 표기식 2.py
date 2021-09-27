import sys

n = int(sys.stdin.readline()) # n의 개수
postfixs = sys.stdin.readline().rstrip() # 후위 표기식 입력 받음 / enter는 제외
numbers = [int(sys.stdin.readline()) for _ in range(n)] # 피연산자에 대응하는 값
stack = []

for postfix in postfixs:
    if postfix.isalpha(): # 만약 알파벳이라면 stack에 저장
        stack.append(numbers[ord(postfix) - ord('A')]) # numbers의 인덱스에 해당되는 값 저장
    else:
        num2 = stack.pop() # 숫자라면 pop()
        num1 = stack.pop()
        if postfix == '+': # 연산자가 +라면 두 값을 더함
            stack.append(num1+num2)
        elif postfix == '-': # 연산자가 -라면 두 값을 뺌
            stack.append(num1-num2)
        elif postfix == '*': # 연산자가 *라면 두 값을 곱함
            stack.append(num1*num2)
        else: # 연산자가 /라면 두 값을 나눔
            stack.append(num1/num2)
print('{0:0.2f}'.format(stack[-1])) # 소수점 둘째자리까지 출력