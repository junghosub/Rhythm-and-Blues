# 주사위를 굴리는 함수
def roll(d):
    if d==1: # 동쪽
        dice[0],dice[2],dice[3],dice[5] = dice[3],dice[0],dice[5],dice[2]
    elif d==2: # 서쪽
        dice[0],dice[2],dice[3],dice[5] = dice[2],dice[5],dice[0],dice[3]
    elif d==3: # 북쪽
        dice[0],dice[1],dice[4],dice[5] = dice[4],dice[0],dice[5],dice[1]
    else: # 남쪽
        dice[0],dice[1],dice[4],dice[5] = dice[1],dice[5],dice[0],dice[4]

# 주사위를 옮기는 함수
def move(x,y):
    for i in direction:
        nx = x + dx[i-1]
        ny = y + dy[i-1]

        # 범위를 벗어나는 종료
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        # 주사위 굴림
        roll(i)
        # 만약 해당 칸이 0이라면, 주사위 밑면의 값으로 대체
        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[5]
        # 해당 칸이 0이 아니면 주사위 밑면을 칸의 값으로 대체 후, 해당 칸은 0
        else:
            dice[5] = graph[nx][ny]
            graph[nx][ny] = 0
        x, y = nx, ny
        print(dice[0])

# 세로의 개수 n, 가로의 개수 m, 위치 (x,y), 명령의 개수 k
n, m, x, y, k = map(int, input().split())

# 그래프 생성
graph = [[] * m for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, input().split()))

# 방향 명령
direction = list(map(int, input().split()))

# 주사위 전개도
dice = [0] * 6

# 방향벡터
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

move(x,y)