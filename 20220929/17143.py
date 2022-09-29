import copy
n,m,s = map(int,input().split())
board = [[[] for _ in range(m+1)] for _ in range(n+1)]




for _ in range(s):
    x,y,speed,direction,size = map(int,input().split())
    board[x][y].append([size,direction,speed])

abgler = 0
abgler_shark_size = 0
while abgler < m:
    nextBoard = copy.deepcopy(board)
    abgler += 1
    for i in range(1,n+1):
        if len(board[i][abgler]) > 0:
            print(board[i][abgler][0][0])
            abgler_shark_size += board[i][abgler][0][0]
            board[i][abgler] = []
            break
    
    #for i in range()
print(abgler_shark_size)
for i in board:
    print(i)
