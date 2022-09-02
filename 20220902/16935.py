n,m,r = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
command = list(map(int,input().split()))

def one(board):
    board.reverse()
    return board

def two(board):
    for i in range(len(board)):
        board[i].reverse()
    return board

def three(board):
    b = []
    for j in range(m):
        bo = []
        for i in range(n):
            bo.append(board[i][j])
        bo.reverse()
        b.append(bo)
    return b

def four(board):
    b = []
    for j in range(m-1,-1,-1):
        bo = []
        for i in range(n):
            bo.append(board[i][j])
        b.append(bo)
    return b

def five(board):
    b = [[0]*m for _ in range(n)]
    nx = [0,n//2,0,-n//2]
    ny = [m//2,0,-m//2,0]
    rgx = [[0,n//2],[0,n//2],[n//2,n],[n//2,n]]
    rgy = [[0,m//2],[m//2,m],[m//2,m],[0,m//2]]
    for k in range(4):
        for i in range(rgx[k][0],rgx[k][1]):
            for j in range(rgy[k][0],rgy[k][1]):
                b[i+nx[k]][j+ny[k]] = board[i][j]
    return b

def six(board):
    b = [[0]*m for _ in range(n)]

    nx = [n//2,0,-n//2,0]
    ny = [0,-m//2,0,m//2]
    rgx = [[0,n//2],[0,n//2],[n//2,n],[n//2,n]]
    rgy = [[0,m//2],[m//2,m],[m//2,m],[0,m//2]]
    for k in range(4):
        for i in range(rgx[k][0],rgx[k][1]):
            for j in range(rgy[k][0],rgy[k][1]):
                b[i+nx[k]][j+ny[k]] = board[i][j]
    return b


for i in command:
    if i == 1 :
        board = one(board)
    elif i == 2 :
        board = two(board)
    elif i == 3 :
        board = three(board)
        a = m
        m = n
        n = a
    elif i == 4 :
        board = four(board)
        a = m
        m = n
        n = a
    elif i == 5 :
        board = five(board)
    elif i == 6 :
        board = six(board)





for b in board :
    print(" ".join(list(map(str,b))))