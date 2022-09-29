from collections import deque
from sys import stdin
from copy import deepcopy
n,m = map(int,input().split())
board = [list(map(int,stdin.readline().split())) for _ in range(n)]

nxt = [(0,1),(1,0),(-1,0),(0,-1)]

def gonggi(board):
    gBoard = [[-1 for _ in range(m)] for _ in range(n)]
    q = deque()

    q.append((0,0))
    while q :
        x,y = q.popleft()
        for nx,ny in nxt:
            dx,dy = x+nx,y+ny
            if 0<=dx<n and 0<=dy<m and board[dx][dy] == 0 and gBoard[dx][dy] == -1:
                q.append((dx,dy))
                gBoard[dx][dy] = 0
    return gBoard



def check(board):
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 :
                return True
    return False

def go(board):
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    cBoard = deepcopy(board)
    q = deque()
    q.append((0,0))
    gBoard = gonggi(board)
    while q :
        x,y = q.popleft()
        for dx,dy in nxt :
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1 and board[nx][ny] == 1 :
                ctn = 0
                for ox,oy in nxt:
                    zx,zy = ox+nx,oy+ny
                    
                    if 0<=zx<n and 0<=zy<m and gBoard[zx][zy] == 0:
                        ctn += 1
                if ctn >= 2 :
                    cBoard[nx][ny] = 0
                visited[nx][ny] = 0
            elif 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1 and board[nx][ny] == 0 :
                q.append((nx,ny))
                visited[nx][ny] = 0
    
    return cBoard

count = 0
while check(board):
    board = go(board)
    count += 1
print(count)
