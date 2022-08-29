import collections
import sys
n = int(input())
g = int(input())
check = [[] for _ in range(n+1)]
board = [list(map(int,sys.stdin.readline().split())) for _ in range(g)]
result = [[0]*n for _ in range(n)]
for b in board:
    if result[b[0]-1][b[1]-1] != 0 :
        result[b[0]-1][b[1]-1] = min(b[2],result[b[0]-1][b[1]-1])
    else :
        result[b[0]-1][b[1]-1] = b[2]
rs = [[10**10]*n for _ in range(n)]
daum = [True for _ in range(n)]

def dfs(x,gx,cost):
    daum[x] = False
    for i in range(n):
        if 0 != result[x][i] and daum[i]:
            rs[gx][i] = min(rs[gx][i],cost+result[x][i])
            dfs(i,gx,cost+result[x][i])
    
    daum[x] = True
for i in range(n):
    dfs(i,i,0)

for r in rs :
    a = " ".join(list(map(str,r)))
    a=a.replace("10000000000","0")
    print(a)
    
