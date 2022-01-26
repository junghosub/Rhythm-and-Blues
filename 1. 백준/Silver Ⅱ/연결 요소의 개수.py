import sys
sys.setrecursionlimit(10**5)

def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True

    # dfs 탐색 시작
    for i in graph[v]:
        # 방문하지 않은 노드 dfs
        if not visited[i]:
            dfs(graph, i, visited)

# 정점의 개수 n, 간선의 개수 m
n, m = map(int, input().split())

# 그래프 생성
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 처리를 저장할 visited
visited = [False for _ in range(n+1)]

# 연결 요소의 개수 cnt
cnt = 0
# 1번 노드부터 n번까지 dfs 탐색
for i in range(1, n+1):
    # dfs이므로 방문처리 되지 않은 노드는 다른 연결요소임.
    if not visited[i]:
        dfs(graph, i, visited)
        cnt += 1
print(cnt)