import collections
import sys
import copy
input = sys.stdin.readline
n,m = map(int,input().strip().split())

boarda = [list(map(int,input().strip().split())) for _ in range(n)]
check = [[0]*m for _ in range(n)]
nx = [0,1,0,-1]
ny = [1,0,-1,0]

def go(board):
    nextBoard = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                ctn = 0
                for k in range(4):
                    dx,dy = i+nx[k],j+ny[k]
                    if 0 <= dx < n and 0 <= dy < m and board[dx][dy] == 0 :
                        ctn += 1
                nextBoard[i][j] = max(0,board[i][j]-ctn)
    return nextBoard

def bfs(board):
    count = 0
    bb = copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            
            if bb[i][j] > 0 and count == 0:
                st = collections.deque()
                st.append((i,j))
                bb[i][j] = -1
                while st :
                    x,y = st.popleft()
                    for k in range(4):
                        dx,dy = x+nx[k],y+ny[k]
                        if 0 <= dx < n and 0 <= dy < m and bb[dx][dy] > 0 :
                            st.append((dx,dy))
                            bb[dx][dy] = -1
                count += 1
            if bb[i][j] > 0 and count > 0 :
                return False
    return True
ccc = 0
while bfs(boarda):
    boarda = go(boarda)
    if boarda == check :
        ccc = 0
        break
    ccc += 1

print(ccc)