import sys
sys.setrecursionlimit(10**6)

def dfs(x,y, num):
    # 방문처리
    visited[x][y] = 1

    # DFS 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 넘어서면 종료
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        # 해당 수위를 넘고, 미방문지역이면 DFS 탐색 진행
        if graph[nx][ny] > num and visited[nx][ny] == 0:
            dfs(nx,ny, num)

# N x N 그래프 생성
n = int(input())
graph =[[] * n for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

# 상,하,좌,우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

res = 0
# 최대의 안전 영역을 찾기 위해 수위 조절
for num in range(max(map(max, graph)) + 1):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and graph[i][j] > num:
                dfs(i,j,num)
                cnt += 1
    if cnt > res:
        res = cnt
print(res)