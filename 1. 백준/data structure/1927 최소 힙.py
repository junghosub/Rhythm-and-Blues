import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(heap, x)
    else:
        print(heapq.heappop(heap) if heap else 0)