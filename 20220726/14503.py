n,m = map(int,input().split())
r,c,w = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

#북동남서 0123
nextX = [-1,0,1,0]
nextY = [0,1,0,-1]



nextW = w
check = True
count = 0
while check :
    board[r][c] = 2
    whoCheck = False
    for i in range(4):
        if nextW == 0 :
            nextW = 3
        else :
            nextW -=1
        if 0 == board[r+nextX[nextW]][c+nextY[nextW]]:
            r = r+nextX[nextW]
            c = c+nextY[nextW]
            break
        
        if i == 3 :
            whoCheck = True
    
    if whoCheck :
        if 1 == board[r+(nextX[nextW]*-1)][c+(nextY[nextW]*-1)]:
            check=False
            break
        else :
            r = r+(nextX[nextW]*-1)
            c = c+(nextY[nextW]*-1)


ccc = 0
for b in board :
    ccc+=b.count(2)
print(ccc)