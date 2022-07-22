n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(m)]
inBoard = board

def check(inBoard) :
    change = 1
    x = [1,0,-1,0]
    y = [0,1,0,-1]
    while change != 0 :
        change = 0
        for i in range(n):
            for j in range(m):
                for a in range(4):
                    if n > i+x[a] >= 0 and m > j+y[a] >= 0:
                        if    inBoard[i][j] == 2 and 0 == inBoard[i+x[a]][j+y[a]] :
                            inBoard[i+x[a]][j+y[a]] = 2
                            change += 1
        print(inBoard)
        result = 0
        for i in range(n):
            result += inBoard[i].count(0)
        return result
selectIdx = [0,0,0]
aaa = 0
bbb = 0

check(board)
print(board)

'''
def go(index):
    global aaa
    global bbb
    global selectIdx
    global n
    global m
    global board
    if sum(selectIdx) == 3 :
        print(board)
        if aaa < check(board):
            aaa = check(board)
        bbb += 1
        return
    else :
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0 :
                    board[i][j] = 1
                    selectIdx[index] = 1
                    go(index+1)
                    board[i][j] = 0
                    selectIdx[index] = 0

go(0)
print(aaa)
print(bbb)
'''