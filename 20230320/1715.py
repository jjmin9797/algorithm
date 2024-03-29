import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n = int(input())
cards = [int(input()) for _ in range(n)]
heap = []
for card in cards:
    heappush(heap, card)
if len(cards) == 1 :
    print(0)
else :
    answer = 0
    while len(heap) > 2:
        firstCard = heappop(heap)
        secondCard = heappop(heap)
        nextCard = firstCard + secondCard
        answer += nextCard
        heappush(heap, nextCard)
    answer += sum(heap)
    print(answer)
