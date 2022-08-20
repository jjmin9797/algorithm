n,m=map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]
check = [[True] * m for _ in range(n)]
print(check)
print(board)
check[0][0] = False

nx = (0,1,0,-1)
ny = (1,0,-1,0)
count = 0

def dfs(x,y) :
    global count
    if x == n-1 and y == m-1 :
        count += 1
        return
    for i in range(4):
        print(nx[i])
        if n-1 >= x+nx[i] >=0 and m-1 >= y+ny[i] >= 0  :
            if board[x+nx[i]][y+ny[i]] < board[x][y] and check[x+nx[i]][y+ny[i]] :
                check[x+nx[i]][y+ny[i]] = False
                dfs(x+nx[i],y+ny[i])
                check[x+nx[i]][y+ny[i]] = True
dfs(0,0)
print(count)
