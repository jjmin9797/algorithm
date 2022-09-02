import sys
input = sys.stdin.readline
n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
check = [True for _ in range(n+1)]
ga = [0 for _ in range(n+1)]

for _ in range(m):
    a,b,w = map(int,input().split())
    graph[a].append([b,w])

def dfs(start,cost,end):
    global maxCost
    if cost > maxCost :
        return

    if start == end :
        maxCost = min(maxCost,cost)
        return

    for i in graph[start]:
        if check[i[0]]:
            check[i[0]] = False
            dfs(i[0],cost+i[1],end)
            check[i[0]] = True
    
for i in range(1,n+1):
    
    check[i] = False
    maxCost = 10**10
    dfs(i,0,x)
    ga[i] = maxCost
    check[i] = True

    check[x] = False
    maxCost = 10**10
    dfs(x,0,i)
    ga[i] += maxCost
    check[x] = True

print(max(ga))
