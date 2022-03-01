from collections import deque

def bfs(queue):
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[x][y] == 1 and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

def checking(graph, visited):
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 0 and visited[i][j] == 0:
                return True

n, m = map(int, input().split())
graph = [[] for _ in range(m)]
for i in range(m):
    tomato = list(map(int, input().split()))
    graph[i] = tomato

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0] * n for _ in range(m)]
queue = deque()
for i in range(m):
    for j in range(n):
        if not visited[i][j] and graph[i][j] == 1:
            queue.append((i,j))
bfs(queue)

if checking(graph, visited):
    print(-1)
else:
    print(max(map(max, visited)))


###
from collections import deque

def bfs(queue):
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 상자의 범위를 넘어서면 종료
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 빈 칸이라면 종료
            if graph[nx][ny] == -1:
                continue
            # 익지않은 토마토 -> 익은 토마토
            if graph[x][y] == 1 and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

# 모든 토마토가 익었는지 확인
def checking(grarph, visited):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 and visited[i][j] == 0:
                return True

# 상자의 가로 m, 상자의 세로 n
m, n = map(int, input().split())
# 상자를 담을 그래프
graph = [[] * m for _ in range(n)]
for i in range(n):
    tomato = list(map(int, input().split()))
    graph[i] = tomato

# 탐색 횟수와 방문여부를 체크할 visited
visited = [[0] * m for _ in range(n)]

# 상,하,좌,우 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 익은 토마토 (시작 노드가 여러 개인 경우)
queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))

# bfs 탐색
bfs(queue)

# 정답 출력
if checking(graph, visited):
    print(-1)
else:
    print(max(map(max, visited)))