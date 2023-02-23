import sys
from heapq import heappop, heappush

input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [float("inf") for _ in range(n + 1)]
visited[0] = 0
heap = []
heappush(heap, (0, 1))
for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append([c, e])
    graph[e].append([c, s])

while heap:
    cost, now = heappop(heap)
    for nCost, nNode in graph[now]:
        if nCost + cost < visited[nNode]:
            visited[nNode] = nCost + cost
            heappush(heap, (nCost + cost, nNode))

print(visited[n])
