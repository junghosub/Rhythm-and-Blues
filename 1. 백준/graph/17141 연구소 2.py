from collections import deque

# m개의 바이러스를 놓는 함수
def dfs(cur, cnt):
    if cnt == m:
        bfs()    
        return
    for i in range(cur, len(virus)):
        pick[i] = 1
        dfs(i + 1, cnt + 1)
        pick[i] = 0

# bfs 탐색
def bfs():
    global res

    queue = deque()
    backup = [backup[:] for backup in visited]

    # 후보로 선정되었으면 queue에 담음
    for i in range(len(pick)):
        if pick[i]:
            queue.append(virus[i])
    
    # queue에 담긴 좌표를 0으로 업데이트
    for i, j in queue:
        backup[i][j] = 0

    # BFS 탐색
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어낫거나 벽, 초기 바이러스를 놓은 좌표면 종료
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if backup[nx][ny] == '-' or backup[nx][ny] == 0:
                continue
            # 탐색 시간 업데이트 후, queue에 push
            if backup[nx][ny] == -1:
                backup[nx][ny] = backup[x][y] + 1
                queue.append((nx, ny))

    # 모든 곳에 바이러스가 퍼졌는지 확인하는 과정
    for i in range(n):
        for j in range(n):
            if backup[i][j] == '-':
                backup[i][j] = 0
            # 만약 안전 지역이 존재하다면 return으로 종료
            if backup[i][j] == -1:
                return
    
    res = min(res, max(map(max, backup)))

# 연구소의 크기 n과 바이러스의 개수 m
n, m = map(int, input().split())

# 연구소의 상태를 담은 그래프 생성
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 바이러스 좌표를 담는 리스트
virus = []

# 탐색 시간을 담을 visited
visited = [[-1] * n for _ in range(n)]

# 연구소 상태 업데이트
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            visited[i][j] = '-'
        if graph[i][j] == 2:
            virus.append((i,j))

# 총 10개의 바이러스 후보
pick = [0] * len(virus)

# 방향벡터
dx = [-1,1,0,0]
dy = [0,0,-1,1]

res = int(1e9)
dfs(0,0)

if res == int(1e9):
    print(-1)
else:
    print(res)