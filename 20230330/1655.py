import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n = int(input())
leftHeap = []
rightHeap = []
answer = []
for i in range(n):
    nextNumber = int(input())
    if len(leftHeap) == len(rightHeap):
        heappush(leftHeap, (-nextNumber, nextNumber))
    else:
        heappush(rightHeap, (nextNumber, nextNumber))
    print(leftHeap, rightHeap)
    if rightHeap and leftHeap[0][1] > rightHeap[0][0]:
        minValue = heappop(rightHeap)[0]
        maxValue = heappop(leftHeap)[1]
        heappush(leftHeap, (-minValue, minValue))
        heappush(rightHeap, (maxValue, maxValue))
    print(leftHeap, rightHeap)
    print()
    answer.append(leftHeap[0][1])
for a in answer:
    print(a)


# 1 ->1
# 1 5 -> 1
# 1 2 5 -> 2
# 1 2 5 10 -> 2
# -99 1 2 5 10 -> 2
# -99 1 2 5 7 10 -> 2
