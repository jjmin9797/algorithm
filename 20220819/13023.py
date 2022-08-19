import sys
n,m = map(int,input().split())
gp = [[] for _ in range(n)]
for i in range(m):
    s,e = map(int,input().split())
    gp[s].append(e)
    gp[e].append(s)
check = [True] * n
sunser = []

def dfs(start):
    sunser.append(start)
    check[start] = False
    for i in gp[start]:
        if check[i] :
            dfs(i)
    
print(gp)       
dfs(0)
print(sunser)
