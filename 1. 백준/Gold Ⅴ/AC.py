import sys
from collections import deque

def isError(func, n):
    if n < func.count('D'):
        return True
    return False

def solve(func, deq):
    r = 1

    for i in func:
        if i == 'R':  # R이면 뒤집기
            r += 1
        if i == 'D': # D라면 버리기
            if deq and r%2 != 0:
                deq.popleft()
            elif deq and r%2 == 0:
                deq.pop()
    else:
        if r%2!=0:
            return str(list(deq))
        else:
            return str(list(reversed(deq)))


t = int(sys.stdin.readline()) # 테스트의 개수

for _ in range(t):
    func = str(sys.stdin.readline().rstrip())
    n = int(sys.stdin.readline().rstrip()) # 배열의 들어있는 수의 개수
    array = sys.stdin.readline().lstrip('[').rstrip(']\n') # 괄호 삭제
    if n == 0:
        deq = deque([])
    else:
        deq = deque(list(map(int, array.split(','))))

    if isError(func, n):
        print('error')
    else:
        print(solve(func, deq).replace(' ',''))
