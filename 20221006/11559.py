import collections
import copy
board = [["." for _ in range(12)] for _ in range(6)]
nxt = [(0,1),(1,0),(-1,0),(0,-1)]

for j in range(12):
    a = input()
    for i in range(len(a)) :
        board[i][j] = a[i]

def bfs(board):
    visited = [[True for _ in range(12)] for _ in range(6)]
    pang = 0
    for i in range(6):
        for j in range(12):
            if board[i][j] != "." and visited[i][j]:
                color = board[i][j]
                ctn = 1
                visited[i][j] = False
                changeBoard = [[i,j]]
                q = collections.deque()
                q.append((i,j))
                while q :
                    x,y = q.popleft()
                    for nx,ny in nxt :
                        dx,dy = x+nx,y+ny
                        if 0<=dx<6 and 0<=dy<12 and board[dx][dy] == color and visited[dx][dy] :
                            q.append((dx,dy))
                            visited[dx][dy] = False
                            ctn += 1
                            changeBoard.append([dx,dy])
                if ctn >= 4 :
                    pang += 1
                    for cx,cy in changeBoard:
                        board[cx][cy] = "."
    return pang,board
                
def boardMove(board):
    rtBoard = []
    for i in range(len(board)):
        q = collections.deque(board[i])
        n = ""
        while q :
            a = q.pop()
            if "." != a :
                n += a
        n = list(n)
        n.reverse()
        n = ["." for _ in range(12-len(n))] + n
        rtBoard.append(n)
    return rtBoard

result = 0
while True :
    pang,board = bfs(board)
    if pang == 0 :
        print(result)
        break
    result += 1
    board = boardMove(board)
    for bbb in board:
        print(bbb)
    print()