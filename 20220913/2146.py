import collections
import sys
sys.setrecursionlimit(10 ** 9)
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
nx = [0,1,0,-1]
ny = [1,0,-1,0]



def bfs(x,y,num):
    visited[x][y] = 1
    graph[x][y] = num
    st = collections.deque()
    st.append((x,y))
    while st :
        x,y = st.popleft()
        for i in range(4):
            dx,dy = x+nx[i],y+ny[i]
            if 0 <= dx < n and 0 <= dy < n and visited[dx][dy] == 0 and graph[dx][dy] == 1 :
                visited[dx][dy] = 1
                graph[dx][dy] = num
                st.append((dx,dy))
minval = 10**10
def dari(x,y,w,co):
    global minval
    visited[x][y] = 1
    st = collections.deque()
    st.append((x,y,w))
    while st :
        x,y,w = st.popleft()
        for i in range(4):
            dx,dy = x+nx[i],y+ny[i]
            if 0 <= dx < n and 0 <= dy < n and graph[dx][dy] == 0 and visited[dx][dy] == 0:
                visited[dx][dy] = 1
                dari(dx,dy,w+1,co)
                
            elif 0 <= dx < n and 0 <= dy < n and graph[dx][dy] != 0 and graph[dx][dy] != co and visited[dx][dy] == 0:
                if minval > w :
                    minval = w
                
                


visited = [[0 for _ in range(n)] for _ in range(n)]
code = 2
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 :
            bfs(i,j,code)
            code += 1
rs = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0 :
            visited = [[0 for _ in range(n)] for _ in range(n)]
            dari(i,j,0,graph[i][j])


print(minval-1)