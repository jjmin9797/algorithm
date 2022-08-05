n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

size = 2

def checkNext(inBoard,a,inSize) :
    rtList = []
    shark = 9999
    for i in range(a):
        for j in range(a):
            if 0 < inBoard[i][j] < inSize :
                rtList.append([i,j])
            elif inBoard[i][j] == 9 :
                shark = [i,j]
    return rtList,shark



while True :
    nextEat,sharkWhere = checkNext(board,n,size)
    

    break
    
            

print(sharkWhere,nextEat)