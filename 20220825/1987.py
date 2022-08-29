import collections
import sys
sys.setrecursionlimit(10**9)
n,m = map(int,input().split())

board = [list(input()) for _ in range(n)]
checkBoard = [[True]*m for _ in range(n)]

nx = [0,1,0,-1]
ny = [1,0,-1,0]
checkBoard[0][0] = False
check = collections.deque()
check.append(board[0][0])
maxCtn = -1
def dfs(x,y,ctn) :
    global maxCtn
    if maxCtn < ctn :
        maxCtn = ctn


    for i in range(4):
        dx = x+nx[i]
        dy = y+ny[i]
        if 0<=dx<n and 0<=dy<m and board[dx][dy] not in check and checkBoard[dx][dy]:
            checkBoard[dx][dy] = False
            check.append(board[dx][dy])
            dfs(dx,dy,ctn+1)
            checkBoard[dx][dy] = True
            check.pop()
dfs(0,0,1)
print(maxCtn)

