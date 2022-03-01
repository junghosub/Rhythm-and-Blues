# 1. 새로 벽을 3개 세운다.
# 2. 바이러스는 상,하,좌,우로 퍼진다.
# 3. 바이러스가 다 퍼진 후, 안전 영역의 최대 크기를 구하여라.

from collections import deque

def dfs(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                dfs(cnt + 1)
                graph[i][j] = 0

def bfs():
    # 큐 생성
    queue = deque()
    backup = [backup[:] for backup in graph]
    visited = [[0] * m for _ in range(n)]

    # 바이러스인 좌표를 queue에 추가
    for i in range(n):
        for j in range(m):
            if backup[i][j] == 2:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()

        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 초과하거나 벽이면 종료!
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if backup[nx][ny] == 1:
                continue
            # 방문처리 되지 않았고, 빈 칸인 곳에 바이러스 퍼짐
            if visited[nx][ny] == 0 and backup[nx][ny] == 0:
                backup[nx][ny] = 2
                visited[nx][ny] = 1
                queue.append((nx, ny))

    # 안전 영역 구하기
    global res
    cnt = 0
    for i in range(n):
        for j in range(m):
            if backup[i][j] == 0:
                cnt += 1
    res = max(res, cnt)

# 세로 크기 n과 가로 크기 m
n, m = map(int, input().split())

# 그래프 생성
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 방향 벡터 설정
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# res의 초기값 설정
res = 0

# 함수 실행
dfs(0)

# 정답 출력
print(res)