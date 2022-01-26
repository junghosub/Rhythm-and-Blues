from collections import deque

# bfs 탐색
def bfs(x, y):
    queue = deque()
    # queue에 추가
    queue.append((x,y))
    # queue가 빌 때까지 탐색
    while queue:
        x, y = queue.popleft()

        # 상,하,좌,우로 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나면 탐색 불가
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽이면 탐색 불가
            if graph[nx][ny] == 0:
                continue

            # 벽이면 탐색
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))