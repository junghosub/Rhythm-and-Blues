import sys
sys.setrecursionlimit(10**5)

# dfs
def dfs(x, y):
    # 방문 처리
    visited[x][y] = True
    # 상,하,좌,우 dfs 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 그리드의 크기를 넘어서면 종료
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        # 방문하지 않았고, 색상이 같으면 계속 탐색
        if visited[nx][ny] == False and graph[nx][ny] == graph[x][y]:
            dfs(nx, ny)

# 그리드의 크기 n
n = int(input())
# 그래프 생성
graph = [[] for _ in range(n)]
for i in range(n):
    colors = list(map(str, input()))
    graph[i] = colors

# 탐색을 위한 방향벡터 (상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 방문 여부를 처리할 visited
visited = [[False] * n for _ in range(n)]
# 구역의 개수 cnt
non_rg_cnt, rg_cnt = 0,0

## 적록색약이 아닌 경우부터 탐색
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            non_rg_cnt += 1

## R - > G로 대체
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

## 적록색약인 경우 탐색
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            rg_cnt += 1
print(non_rg_cnt, rg_cnt)