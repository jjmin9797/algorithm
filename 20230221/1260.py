import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
routes = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n + 1)]

for s, e in routes:
    graph[s].append(e)
    graph[e].append(s)

for i in range(n + 1):
    graph[i].sort()


def bfs(v, graph, n):
    queue = deque()
    queue.append(v)
    visited = [False for _ in range(n + 1)]
    visited[v] = True
    answer = []
    while queue:
        nxt = queue.popleft()
        answer.append(nxt)
        for x in graph[nxt]:
            if not visited[x]:
                visited[x] = True
                queue.append(x)

    return answer


answer = []
visited2 = [False for _ in range(n + 1)]


def dfs(s, graph, n):
    visited2[s] = True
    answer.append(s)
    for x in graph[s]:
        if not visited2[x]:
            dfs(x, graph, n)


bfs_result = bfs(v, graph, n)

dfs(s, graph, n)
print(" ".join(map(str, answer)))
print(" ".join(map(str, bfs_result)))
