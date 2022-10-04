from itertools import combinations
import copy
import collections
n,m,d = map(int,input().split())
mainBoard = [list(map(int,input().split())) for _ in range(n)]
#board.append([0 for _ in range(m)])
where = [i for i in range(m)]
archers = []
for i in combinations(where,3):
    archers.append(i)
na = [(0,-1),(-1,0),(0,1)]

def check(board) :
    for i in range(n):
        for j in range(m):
            if board[i][j]==1:
                return True
    return False



for archer in archers:
    ctn = 0
    board = copy.deepcopy(mainBoard)
    for a in archer:
        while check(board):
            nextBoard = copy.deepcopy(board)
            q = collections.deque()
            q.append((n-1,a,1))
            visited = [[0 for _ in range(m)] for _ in range(n)]
            visited[n-1][a] = -1
            while q :
                x,y,w = q.popleft()
                if w > d:
                    break
                if board[x][y] == 1:
                    if nextBoard[x][y] == 0:
                        break
                    else :
                        nextBoard[x][y] = 0
                        ctn += 1
                    break
                for nx,ny in na :
                    dx,dy = x+nx,y+ny
                    if 0<=dx<n and 0<=dy<m and visited[dx][dy] == 0:
                        q.append((dx,dy,w+1))
                        visited[dx][dy] = -1
            nextBoard = [[0 for _ in range(m)]] + nextBoard
            nextBoard.pop()
            board = copy.deepcopy(nextBoard)
            for bbb in board:
                print(bbb)
            print()
        print(ctn)
            