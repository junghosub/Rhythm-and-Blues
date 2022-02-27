def dfs(cur, cnt):
    global res
    # n//2로 나누어진 팀의 개수
    if cnt == n//2:
        # 점수를 구해줌
        start, link = 0, 0

        for i in range(n):
            for j in range(i+1, n):
                if visited[i] and visited[j]:
                    start += (graph[i][j] + graph[j][i])
                elif not visited[i] and not visited[j]:
                    link += (graph[i][j] + graph[j][i])
        res = min(res, abs(start - link))
        return 

    # 백트래킹 실시
    for i in range(cur, n):
        visited[i] = 1
        dfs(i + 1, cnt + 1)
        visited[i] = 0

# 모인 인원 수 n
n = int(input())

# 능력치 그래프
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 백트래킹을 위한 리스트
visited = [0] * n
# 점수
res = int(1e9) 
dfs(0,0)
print(res)