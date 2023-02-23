def check(board) :
    whiteStartBoard = ['W','B','W','B','W','B','W','B']
    blackStartBoard = ['B','W','B','W','B','W','B','W']
    count = [0,0]
    for i in range(8) :
        for j in range(8) :
            if i % 2 == 0 and board[i][j] != whiteStartBoard[j] :
                count[0] += 1
            elif i % 2 == 1 and board[i][j] != blackStartBoard[j] :
                count[0] += 1
        for j in range(8) :
            if i % 2 == 1 and board[i][j] != whiteStartBoard[j] :
                count[1] += 1
            elif i % 2 == 0 and board[i][j] != blackStartBoard[j] :
                count[1] += 1


    

    return min(count)


n,m = map(int,input().split())
board = [input() for _ in range(n)]
ans = 1000
for i in range(0,n-7) :
    for j in range(0,m-7) :
        boardY = []
        for x in range(i,i+8) :
            boardX = []
            for y in range(j,j+8):
                
                boardX.append(board[x][y])
            boardY.append(boardX)
        ctn = check(boardY)
        if ctn < ans:
            ans = ctn
print(ans)
    