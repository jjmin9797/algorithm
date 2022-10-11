import collections
import copy
n,m,t = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
zeroCount = 0
totalNumber = n*m
result = 0
nxt = [(0,1),(1,0),(0,-1),(-1,0)]
def eliminate(board):
    rtBoard = copy.deepcopy(board)
    global totalNumber
    zc = 0
    for i in range(n):
        for j in range(m):
            
            for nx,ny in nxt :
                dx,dy = nx+i,ny+j
                if dy < 0:
                    dy = m-1
                elif dy > m-1 :
                    dy = 0
                if 0<= dx < n and board[i][j] == board[dx][dy] and board[i][j] != 0:
                    if rtBoard[dx][dy] != 0 :
                        zc += 1
                        totalNumber -= 1
                    rtBoard[dx][dy] = 0
                    
                    
    return zc,rtBoard


def turn(x,d,k,board):
    rtBoard = copy.deepcopy(board)
    #시계
    if d == 0 :
        for i in range(x-1,n,x):
            q = collections.deque(board[i])
            for _ in range(k):
                q.appendleft(q.pop())
            rtBoard[i] = list(q)
    
    #반시계
    elif d == 1 :
        for i in range(x-1,n,x):

            q = collections.deque(board[i])
            for _ in range(k):
                q.append(q.popleft())
            rtBoard[i] = list(q)
    return rtBoard

def avgChange(board):
    global totalNumber
    hap = 0
    for b in board:
        hap += sum(b)
    if totalNumber == 0 :
        return board
    avg = hap / totalNumber

    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and avg < board[i][j]:
                board[i][j] -= 1
            elif board[i][j] != 0 and avg > board[i][j]:
                board[i][j] += 1
    return board

for i in range(t):
    x,d,k = map(int,input().split())
    board = turn(x,d,k,board)
    zc,board = eliminate(board)
    if zc == 0 :
        board = avgChange(board)

    zeroCount += zc
for b in board:
    result += sum(b)
print(result)

