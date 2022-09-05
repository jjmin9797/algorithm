import sys

sys.setrecursionlimit(10 ** 9)
n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
check = [-1]*(n+1)
check[1] = -1
def dfs(start,w):

    for nStart,nw in graph[start]:
        if check[nStart] == -1:
            check[nStart] = w+nw
            dfs(nStart,w+nw)

dfs(1,0)
start = check.index(max(check))
check = [-1]*(n+1)
dfs(start,0)
print(max(check))
        
