import sys
from itertools import combinations
from collections import deque


def findCost(c1, c2, graph, n, mcost):
    cost = 0
    for i in range(1, n + 1):
        if i == c1 or i == c2:
            continue
        visited = [True for _ in range(n + 1)]
        queue = deque()
        queue.append((0, i))
        visited[i] = False
        while queue:
            now_cost, now = queue.popleft()
            if now == c1 or now == c2:
                cost += now_cost * 2
                break
            for nNode in graph[now]:
                if visited[nNode]:
                    visited[nNode] = False
                    queue.append((now_cost + 1, nNode))
        if cost > mcost:
            return float("inf")
    return cost


input = sys.stdin.readline
n, m = map(int, input().split())
routes = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n + 1)]
for s, e in routes:
    graph[s].append(e)
    graph[e].append(s)

cases = list(combinations(range(1, n + 1), 2))
answer = []
MIN_COST = float("inf")
for c1, c2 in cases:
    nowCost = findCost(c1, c2, graph, n, MIN_COST)
    if nowCost < MIN_COST:
        answer = [str(c1), str(c2), str(nowCost)]
        MIN_COST = nowCost
print(" ".join(answer))
