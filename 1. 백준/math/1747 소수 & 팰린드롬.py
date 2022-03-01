import sys

a = int(sys.stdin.readline()) # a를 입력받음
palindrome = []

for i in range(a, 1003002): # 팰린드롬을 먼저 생성
    if str(i) == str(i)[::-1]: # 팰린드롬이면 True
        palindrome.append(i)

for i in palindrome:
    check = True
    for j in range(2, int(i**0.5)+1): # 팰린드롬일 경우, 소수 체크(sqrt)
        if i % j == 0:
            check = False
            break
    if check and i > 1:
        print(i)
        break