t = int(input()) # 테스트 데이터 수를 위한 정수 입력

for _ in range(t):
    parens = list(input())
    ptr = 0 # 스택에 들어간 데이터의 개수

    for i in parens:
        if i == '(':
            ptr += 1 # push
        else:
            ptr -= 1 # pop
        if ptr < 0:
            break # 처음에 ')' 나오면 break
    print('YES' if ptr == 0 else 'NO') # '('와 ')'의 수가 맞는다면 ptr을 0일 것이다. 아니라면 NO