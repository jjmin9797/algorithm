import sys
from heapq import heappop, heappush

input = sys.stdin.readline
leftHeap = []
rightHeap = []
answer = []
n = int(input())
for _ in range(n):
    nextNumber = int(input())
    if len(leftHeap) == len(rightHeap):
        heappush(leftHeap, [-nextNumber, nextNumber])
    else:
        heappush(rightHeap, [nextNumber, nextNumber])

    if rightHeap and leftHeap[0][1] > rightHeap[0][0]:
        minValue = heappop(rightHeap)[0]
        maxValue = heappop(leftHeap)[1]
        heappush(leftHeap, [-minValue, minValue])
        heappush(rightHeap, [maxValue, maxValue])

    answer.append(leftHeap[0][1])
for a in answer:
    print(a)
