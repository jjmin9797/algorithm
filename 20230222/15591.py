from collections import deque
from sys import stdin

input = stdin.readline


def bfs(graph, k, v, n):
    queue = deque()
    queue.append((v, float("inf")))
    minUsado = [float("inf") for _ in range(n + 1)]
    minUsado[v] = 0
    minUsado[0] = 0
    visited = [True for _ in range(n + 1)]
    visited[v] = False
    while queue:
        x, mc = queue.popleft()
        for cost, nx in graph[x]:
            if visited[nx]:
                nxtCost = min(cost, mc)
                minUsado[nx] = nxtCost
                queue.append([nx, nxtCost])
                visited[nx] = False
    return len([i for i in minUsado if i >= k])


n, q = map(int, input().split())
usado = [list(map(int, input().split())) for _ in range(n - 1)]
question = [list(map(int, input().split())) for _ in range(q)]
graph = [[] for _ in range(n + 1)]
for s, e, c in usado:
    graph[s].append([c, e])
    graph[e].append([c, s])


for k, v in question:
    print(bfs(graph, k, v, n))
