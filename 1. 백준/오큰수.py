# ai의 오른쪽에 있으면서 ai보다 큰 수 중 왼쪽에 있는 수
import sys
n = int(sys.stdin.readline()) # 수열의 크기
array = list(map(int,sys.stdin.readline().split())) # 수열의 원소를 list 형태로 입력 받음
answer = [-1] * n # 그러한 수가 없는 경우 -1
stk = [0] # index

for i in range(1, n): # idx를 의미하고, stack에 이미 0이 있으므로 1부터 시작
    while stk and array[stk[-1]] < array[i]: # 오른쪽에 있으면서 더욱 큰 수라면
        answer[stk.pop()] = array[i] # stack에 있는 idx에 해당되는 곳에 할당함.
    stk.append(i) # idx 업데이트
print(*(answer)) # 출력