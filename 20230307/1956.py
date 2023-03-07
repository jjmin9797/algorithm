import sys
from heapq import heappop, heappush

input = sys.stdin.readline
v, e = map(int, input().strip().split())
dist = [[float("inf") for _ in range(v + 1)] for _ in range(v + 1)]
graph = [[] for _ in range(v + 1)]
heap = []
for i in range(e):
    s, e, c = map(int, input().strip().split())
    graph[s].append([c, e])
    dist[s][e] = c
    heappush(heap, [c, s, e])

while heap:
    now_cost, now_start, now_end = heappop(heap)

    if now_start == now_end:
        print(now_cost)
        break

    if dist[now_start][now_end] < now_cost:
        continue

    for next_cost, next_node in graph[now_end]:
        new_cost = now_cost + next_cost
        if new_cost < dist[now_start][next_node]:
            dist[now_start][next_node] = new_cost
            heappush(heap, [new_cost, now_start, next_node])
else:
    print(-1)
