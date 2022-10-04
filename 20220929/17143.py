import copy
n,m,s = map(int,input().split())
board = [[[] for _ in range(m+1)] for _ in range(n+1)]

direct = [(-1,0),(1,0),(0,1),(0,-1)]
# 0 -9
# 2,4
# 2,-5
#0,1

for _ in range(s):
    x,y,speed,direction,size = map(int,input().split())
    board[x][y].append([size,direction,speed])
#
def nextLocation(i,j,direction,speed):
    nx,ny = direct[direction-1]
    if direction == 1 :
        speed = speed % ((n*2)-2)
    elif direction == 2 :
        speed = speed % ((n*2)-2)
    elif direction == 3 :
        speed = speed % ((m*2)-2)
    elif direction == 4 :
        speed = speed % ((m*2)-2)
        i,j = i+(nx*speed),j+(ny*speed)
        while not (1<=i<n+1) and not (1<=j<m+1):
            nx *= -1
            ny *= -1
            i,i = i+(nx*speed),j+(ny*speed)
    

    


    pass



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
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if len(board[i][j]) > 0 :
                size,direction,speed = board[i][j][0]
                nextLocation(i,j,direction,speed)

