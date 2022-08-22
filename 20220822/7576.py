from collections import deque
m,n = map(int,input().split())
graph = []
queue = deque([])
for i in range(n):
    graph.append(list(map(int,input().split())))
    
    for j in range(m): #익은 토마토 큐에 저장
        if graph[i][j]==1:
            queue.append([i,j])
            
dx = [-1,1,0,0]
dy = [0,0,-1,1]
print(queue)