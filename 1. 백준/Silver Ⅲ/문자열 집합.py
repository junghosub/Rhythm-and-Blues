# 딕셔너리를 이용한 방법
import sys

n, m = map(int, sys.stdin.readline().split())
cnt = 0

dic = {sys.stdin.readline().strip() for _ in range(n)}

for _ in range(m):
    s = sys.stdin.readline().strip()
    if s in dic:
        cnt += 1
print(cnt)

# 집합을 이용한 방법
import sys

n, m = map(int, sys.stdin.readline().split())
cnt = 0

s = set([sys.stdin.readline().strip() for _ in range(n)])

for _ in range(m):
    check = sys.stdin.readline().strip()
    if check in s:
        cnt += 1
print(cnt)

