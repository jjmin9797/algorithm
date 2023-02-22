import sys
from heapq import heappop, heappush

input = sys.stdin.readline
heap = []
n = int(input())
for _ in range(n):
    for i in list(map(int, input().strip().split())):
        if len(heap) < n:
            heappush(heap, i)
        else:
            if heap[0] < i:
                heappop(heap)
                heappush(heap, i)
print(heap[0])
