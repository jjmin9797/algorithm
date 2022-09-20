import heapq
import sys

n = int(input())
m = int(input())
inf = 1000000
graph = [[] for _ in range(n+1)]
visited = [inf for _ in range(n+1)]
for _ in range(m):
    start,end,w = map(int,sys.stdin.readline().split())
    graph[start].append((end,w))

startCity,endCity = map(int,input().split())

q = []
heapq.heappush(q,[0,startCity])
visited[startCity] = 0

while q:
    
    w,start = heapq.heappop(q)
    if visited[start] < w :
        continue
    for g in graph[start]:
        nx = w+g[1]
        if visited[g[0]] > nx :
            visited[g[0]] =nx
            heapq.heappush(q,[nx,g[0]])
    
print(visited[endCity])