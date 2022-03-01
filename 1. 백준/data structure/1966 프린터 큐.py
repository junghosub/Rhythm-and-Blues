import sys
from collections import deque

# 문제풀이를 위한 함수 생성
def solve(n, m, paper, idx):
    target = idx[m] # target은 몇번째로 인쇄 되는지 궁금한 문서의 위치 (index)
    cnt = 0 # 몇번째로 인쇄되는지 알기 위한 count

    while True:
        if paper[0] == max(paper): # 만약 paper[0]이 max값과 같다면 출력해준다.
            cnt += 1
            if idx[0] == target: # 그런데 인덱스가 target과 같다면 지금까지의 count를 출력해줌.
                return cnt
                break
            else:
                idx.popleft() # max 값과 같기는 한데 index가 다른 것이니 빼준다.
                paper.popleft()
        else:
            paper.append(paper.popleft()) # 만약 max값이 아니라면 queue처럼 뒤로 넘김
            idx.append(idx.popleft()) # index 덱 또한 뒤로 넘김

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    paper = deque(map(int, sys.stdin.readline().split()))
    idx = deque(i for i in range(len(paper)))
    print(solve(n, m, paper, idx))
