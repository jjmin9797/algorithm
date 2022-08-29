n = 8
board = [list(1 for _ in range(n)) for _ in range(n)]
import copy
nx = [1,0,-1,0,-1,1,-1,1]
ny = [0,1,0,-1,-1,1,1,-1]
ctn = 0
def go(x,y,idx):

    global ctn
    if idx == n :
        ctn += 1
        return
    board[x][y] = -1
    for i in range(1,n):
        for j in range(8):
            dx = x+(i*(nx[j]))
            dy = y+(i*(ny[j]))

            if 0<=dx<n and 0<=dy<n:
                board[dx][dy] = -1
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1 :
                go(i,j,idx+1)

for i in range(n):
    for j in range(n):
        board = [list(1 for _ in range(n)) for _ in range(n)]
        go(i,j,1)

print(ctn)
