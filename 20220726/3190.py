n = int(input())
n+=2
board = []
for i in range(n):
    if i == 0 or i == n-1 :
        board.append([1] * n)
    else :
        a = [1]
        for i in range(n-2):
            a.append(0)
        a.append(1)
        board.append(a)
k = int(input())
for i in range(k):
    x,y = map(int,input().split())
    board[x][y] = 2

def next(inNextX,inNextY,where) :
    if inNextX == 0 and inNextY == 1 :
        if where == 'L' :
            return -1,0
        elif where == 'D':
            return 1,0

    elif inNextX == 0 and inNextY == -1 :
        if where == 'L' :
            return 1,0
        elif where == 'D':
            return -1,0

    elif inNextX == -1 and inNextY == 0 :
        if where == 'L' :
            return 0,-1
        elif where == 'D':
            return 0,1
    
    elif inNextX == 1 and inNextY == 0 :
        if where == 'L' :
            return 0,1
        elif where == 'D':
            return 0,-1

time = 0
nextX = 0
nextY = 1
l = int(input())
dummy=[[1,1]]
switchBoard = [input().split() for _ in range(l)]

for j in range(1,10000) :
    for ss in switchBoard :
        if ss[0] == str(time) :
            nextX,nextY = next(nextX,nextY,ss[1])
            break

    checkPointX = dummy[0][0]+nextX
    checkPointY = dummy[0][1]+nextY
    if board[checkPointX][checkPointY] == 1 :
        realBreak = True
        break
    
    elif [checkPointX,checkPointY] in dummy :
        realBreak = True
        break 

    elif board[checkPointX][checkPointY] == 2 :
        board[checkPointX][checkPointY] = 0
        dummy.insert(0,[checkPointX,checkPointY])
        time += 1
        
    elif board[checkPointX][checkPointY] == 0 :
        for ww in range(len(dummy)-2,-1,-1):
            dummy[ww+1] = dummy[ww]
        dummy[0] = [dummy[0][0]+nextX,dummy[0][1]+nextY]
        time += 1
print(time+1)
