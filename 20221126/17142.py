from itertools import combinations
from collections import deque
import copy
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
bs = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2:
            bs.append([0,i,j])
            board[i][j] = -1
        if board[i][j] == 1:
            board[i][j] = -2
        
bsCombinations = list(combinations(bs,m))
nx = [0,1,0,-1]
ny = [1,0,-1,0]
result = []
for bas in bsCombinations:
    copyBoard = copy.deepcopy(board)
    for t,x,y in bas:
        copyBoard[x][y] = -3
    q = deque(bas)
    while q :
        t,x,y = q.popleft()
        for i in range(4):
            dx,dy = x+nx[i],y+ny[i]
            if 0<=dx<n and 0<=dy<n :
                if copyBoard[dx][dy] == 0:
                    copyBoard[dx][dy] = t+1
                    q.append([t+1,dx,dy])
                if copyBoard[dx][dy] == -1:
                    copyBoard[dx][dy] = -3
                    q.append([t+1,dx,dy])
    maxValue = -1
    check = True
    for i in range(n):
        for j in range(n):
            if 1<=copyBoard[i][j]and copyBoard[i][j]>maxValue:
                maxValue = copyBoard[i][j]
            if copyBoard[i][j] == 0 :
                check=False
    
    if check :
        if maxValue == -1 :
            result.append(0)
        else :
            result.append(maxValue)


if len(result) == 0 :
    print(-1)
else :
    print(min(result))
