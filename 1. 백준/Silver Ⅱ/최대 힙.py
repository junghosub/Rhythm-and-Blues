import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(heap, (-x, x))
    else:
        print(heapq.heappop(heap)[1] if heap else 0)