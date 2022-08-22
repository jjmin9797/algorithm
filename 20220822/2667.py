import sys
sys.setrecursionlimit(1000000)
n= int(input())

board = [list(map(int,list(input()))) for _ in range(n)]
check = [[True] * n for _ in range(n)]

nx = [0,1,0,-1]
ny = [1,0,-1,0]
result = []
c = 0
def dfss(x,y):
    check[x][y] = False
    global c
    c += 1
    for i in range(4):
        if 0<= x+nx[i] <= n-1 and 0 <= y+ny[i] <= n-1 :
            if check[x+nx[i]][y+ny[i]] and board[x+nx[i]][y+ny[i]] == 1:
                check[x+nx[i]][y+ny[i]] = False
                dfss(x+nx[i],y+ny[i])
    return c
for i in range(n):
    for j in range(n):
        if check[i][j] and board[i][j] == 1 :
            c = 0
            result.append(dfss(i,j))
result.sort()
print(len(result))
for i in result:
    print(i)