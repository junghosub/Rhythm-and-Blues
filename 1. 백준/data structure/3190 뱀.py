from collections import deque

def change(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4

    return direction

def bfs(x, y):
    direction, time = 1, 1 # 초기 방향(오른쪽)과 시간
    queue = deque()
    queue.append((x,y)) # 초기 방문 위치
    graph[x][y] = 2 # 방문처리

    while queue:
        # 뱀이 움직일 방향
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 만약 벽 또는 몸에 부딪힌다면 종료
        if  0 < nx <= n and 0 < ny <= n and graph[nx][ny] != 2:
            if graph[nx][ny] == 0: # 사과가 없는 경우, 꼬리 제거
                a, b = queue.popleft()
                graph[a][b] = 0
            graph[nx][ny] = 2 # 사과가 있는 경우, 꼬리 늘림
            queue.append((nx, ny))

            if time in times.keys(): # 방향 전환을 해야하는 시간일 때, change 실행
                direction = change(direction, times[time])
            time += 1

            x, y = nx, ny
        else:
            return time

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 보드의 크기 n
n = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]

# 사과의 개수 k
k = int(input())
for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1 # 사과 위치 저장

# 방향 변환 횟수 l
l = int(input())
times = {}
for i in range(l):
    x, c = input().split()
    times[int(x)] = c # 시간과 방향 저장

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(bfs(1,1))