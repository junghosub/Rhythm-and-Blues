from itertools import combinations

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

shop = []
house = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            shop.append((i,j))
        if graph[i][j] == 1:
            house.append((i,j))

res = float('inf')

for candi in list(combinations(shop, m)):
    cnt = 0
    for x1, y1 in house:
        cnt += min([(abs(x1 - x2) + abs(y1 - y2)) for x2, y2 in candi])
    res = min(res, cnt)
print(res)


# dfs를 활용해본 방법이지만 시간 초과가 난다. 최적화 방법을 생각해봐야겠음.
from collections import deque
def dfs(cnt):
    global res

    if cnt == m:
        candi = 0
        for x1, y1 in house:
            candi += min([(abs(x1-x2) + abs(y1-y2)) for x2, y2 in pick])
        res = min(candi, res)
        return 

    for i in range(len(shop)):
        pick.append(shop.pop())
        dfs(cnt + 1)
        shop.appendleft(pick.pop())

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

house = []
shop = deque()
pick = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            shop.append((i,j))
        if graph[i][j] == 1:
            house.append((i,j))
res = float('inf')
dfs(0)
print(res)