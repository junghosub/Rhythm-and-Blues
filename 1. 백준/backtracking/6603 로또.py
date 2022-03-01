from itertools import combinations
import sys

# 6개의 숫자를 고르는 경우의 수
def solution(n, array):
    return combinations(array, 6)

while True:
    t = list(map(int, sys.stdin.readline().split()))
    n = t[0] # 번호의 수
    array = sorted(t[1:]) # 번호
    if n == 0: # 만약 번호가 0이면 종료
        break
    for i in solution(6, array): # 경우의 수 출력
        print(*(i))
    print() # 테스트 케이스 사이의 빈 줄 출력