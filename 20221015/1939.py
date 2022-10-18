import heapq
import sys

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().strip().split())
    graph[a].append([c,b])
    graph[b].append([c,a])
for i in range(1,n+1):
    graph[i].sort(reverse=True)

distance = [0] * (n + 1)
start,end = map(int,input().split())
q = []
heapq.heappush(q,[0,start])
while q :
    dist,now = heapq.heappop(q)
    dist *= -1

    if now == end :
        print(dist)
        break

    if distance[now] > dist :
        continue

    for i in graph[now]:
        nextDist,nextCity = i[0],i[1]
        if dist == 0 :
            distance[nextCity] = nextDist
            heapq.heappush(q,[-distance[nextCity],nextCity])
        elif distance[nextCity] < nextDist and distance[nextCity] < dist :
            distance[nextCity] = min(dist,nextDist)
            heapq.heappush(q,[-distance[nextCity],nextCity])


