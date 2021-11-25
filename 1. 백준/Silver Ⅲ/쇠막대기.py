import sys

bars = list(sys.stdin.readline().rstrip())
stack = []
cnt = 0

for i in range(len(bars)):
    if bars[i] == '(': # 만약 '(' 괄호면 stack에 저장
        stack.append(bars[i])
    else: # ')' 괄호면 레이저 또는 쇠막대기가 끝나는 지점
        if bars[i-1] == '(': # 레이저라면 이전까지 저장된 쇠막대기의 수 저장
            stack.pop()
            cnt += len(stack)
        else: # 쇠막대기라면 끄트머리 +1
            stack.pop()
            cnt += 1
print(cnt)
