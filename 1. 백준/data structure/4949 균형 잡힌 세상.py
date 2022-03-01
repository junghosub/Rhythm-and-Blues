while True:
    string = input()
    if string == '.':
        break
    stk = []

    for s in string:
        if s == '(' or s == '[': # 만약 왼쪽 괄호이면 stack에 저장
            stk.append(s)
        elif s == ')': # 오른쪽 소괄호가 나왔을 때
            if stk and stk[-1] == '(':
                stk.pop()
            else:
                stk.append(s)
        elif s == ']': # 오른쪽 대괄호가 나왔을 때
            if stk and stk[-1] == '[':
                stk.pop()
            else:
                stk.append(s)
    if stk:
        print('no')
    else:
        print('yes')