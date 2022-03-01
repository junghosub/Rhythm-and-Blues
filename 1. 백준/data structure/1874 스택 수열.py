n = int(input())
array = []
res = []
answer = []
ptr = 0

for _ in range(n):
    array.append(int(input()))

for i in array:
    while True:
        if i > ptr: # array의 숫자가 ptr보다 크면 ptr 증가
            ptr += 1
            res.append(ptr)
            answer.append('+')
        elif i == res[-1]: # array의 숫자가 ptr과 같다면 pop 출력
            res.pop()
            answer.append('-')
            break
        else: # array의 숫자가 answer[-1]보다 작으면 NO
            answer.append('NO')
            break

if 'NO' in answer:
    print('NO')
else:
    print(*answer, sep = '\n')