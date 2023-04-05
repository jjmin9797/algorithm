from heapq import heappush, heappop

heap = []
n = int(input())
for _ in range(n):
    commandType = int(input())
    if commandType == 1:
        value = int(input())
        heappush(heap, value)
    elif commandType == 2:
        print(heappop(heap))
