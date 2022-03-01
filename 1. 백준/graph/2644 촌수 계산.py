from collections import deque

# dfs를 통해 탐색하기
def dfs(graph, v, visited):
    global cnt, flag
    # 해당 노드 방문 처리
    visited[v] = True

    for i in graph[v]:
        # 만약 방문하지 않았다면 dfs 탐색
        if not visited[i]:
            dfs(graph, i, visited)
            cnt += 1
        if i == a:
            return cnt
    return -1

# bfs
from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = visited[v] + 1
                queue.append(i)

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
a, b = map(int, input().split())
m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
bfs(graph, a, visited)

if visited[b] > 0 :
    print(visited[b])
else:
    print(-1)