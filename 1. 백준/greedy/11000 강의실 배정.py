# 덱을 활용한 코드. 시간 초과 ㅜㅜ
from collections import deque

def solution():
    queue = deque()
    queue.append(0)
    
    for time in schedule:
        for _ in range(len(queue)):
            if time[0] >= queue[0]:
                queue.popleft()
                queue.appendleft(time[1])
                break
            queue.rotate(-1)
        else:
            queue.append(time[1])
    return len(queue)

n = int(input())
schedule = []
for _ in range(n):
    s, f = map(int, input().split())
    schedule.append([s,f])
schedule.sort(key = lambda x : (x[1], x[0]))
print(solution())

# 최소 힙을 활용한 코드
import heapq

n = int(input())
schedule = []

for _ in range(n):
    s, t = map(int, input().split())
    schedule.append([s, t])
schedule.sort()

heap = [0]

for s, t in schedule:
    if s >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, t)
print(len(heap))