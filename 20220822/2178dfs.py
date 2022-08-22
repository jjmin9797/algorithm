import sys
sys.setrecursionlimit(1000000)
n,m = map(int,input().split())
board = [list(map(int,list(input()))) for _ in range(n)]
check = [[True] * m for _ in range(n)]

minVal = 10**10
nx = [0,1,0,-1]
ny = [1,0,-1,0]
check[0][0] = False
def dfs(x,y,c):
    global minVal
    if x == n-1 and y == m-1 :
        if minVal > c :
            minVal = c
        return
    
    for i in range(4):
        if 0 <= x+nx[i] <= n-1 and 0 <= y+ny[i] <= m-1:
            if check[x+nx[i]][y+ny[i]] and board[x+nx[i]][y+ny[i]] == 1:
                check[x+nx[i]][y+ny[i]] = False
                dfs(x+nx[i],y+ny[i],c+1)
                check[x+nx[i]][y+ny[i]] = True
dfs(0,0,1)
print(minVal)


