import sys

n, m = map(int, sys.stdin.readline().split())

offbrand = dict()
cnt = 0
answer = []

for _ in range(n+m):
    name = sys.stdin.readline().rstrip()
    if name not in offbrand:
        offbrand[name] = 1
    else:
        offbrand[name] += 1

for key, value in offbrand.items():
    if value == 2:
        cnt += 1
        answer.append(key)
answer.sort()
print(cnt)
print(*answer, sep = '\n')