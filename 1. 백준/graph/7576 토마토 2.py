from collections import deque

# bfs 탐색
def bfs(queue):
    # 큐가 빌 때까지 실행
    while queue:
        x, y, z = queue.popleft()

        # 위 칸, 아래 칸, 상,하,좌,우
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            # 범위를 벗어나는 경우에 종료!
            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue
            # 빈 칸인 경우 종료!
            if graph[nx][ny][nz] == -1:
                continue
            # 현재 칸이 익은 토마토이며, 다음 칸이 익지 않은 토마토 & 방문하지 않은 경우, 탐색한다
            if visited[nx][ny][nz] == 0 and graph[x][y][z] == 1 and graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = 1 # 토마토 익음
                visited[nx][ny][nz] = visited[x][y][z] + 1 # 탐색 횟수
                queue.append((nx,ny,nz)) # 큐에 추가

# 모든 토마토가 익었는지 확인
def checking(graph, visited):
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if graph[i][j][k] == 0 and visited[i][j][k] == 0:
                    return True

# 상자의 가로 길이 m, 상자의 세로 길이 n, 상자의 높이 h
m, n, h = map(int, input().split())
# 그래프 생성
graph = [[[] * m for _ in range(n)] for _ in range(h)]
for i in range(h):
    for j in range(n):
        graph[i][j] = list(map(int, input().split()))

# 방문 처리할 visited
visited = [[[0] * m for _ in range(n)] for _ in range(h)]

# 위,아래(z축),상,하,좌,우
dx = [0,0,-1,1,0,0]
dy = [0,0,0,0,-1,1]
dz = [-1,1,0,0,0,0]

# 시작 노드가 여러 개인 경우
queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))
# bfs 탐색 진행
bfs(queue)

# 탐색 횟수의 최댓값 찾기
res = 0
for i in range(h):
    if res < max(map(max, visited[i])):
        res = max(map(max, visited[i]))

# 만약 모든 토마토가 익지 않으면 -1, 익엇으면 최댓값 출력
if checking(graph, visited):
    print(-1)
else:
    print(res)