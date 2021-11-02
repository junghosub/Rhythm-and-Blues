import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
sigma = 0

for a,b,c in combinations(cards, 3): # 조합을 사용하여 모든 가능한 수 구하기
    if abs((a+b+c)-m) < abs(sigma-m) and a+b+c <=m: # 만약 세 수가 m을 넘지 않고, 기존의 값보다 m에 가까우면 변경
        sigma = a+b+c
    if sigma == m: # 만약 m가 똑같으면 종료
        break
print(sigma) # 가장 가까운 값 출력