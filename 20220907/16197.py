n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]
nx = [0,1,0,-1]
ny = [1,0,-1,0]
coins = []
for i in range(n):
    for j in range(m):
        if board[i][j] == "o":
            coins.append([i,j])
minValue = 20
def go (coin1,coin2,ctn) :
    global minValue
    if (0 > coin1[0] or coin1[0] >= n or 0 > coin1[1] or coin1[1] >= m) and (0<=coin2[0]<n and 0 <= coin2[1]<m):
        if minValue > ctn :
            minValue = ctn
        return
    elif (0 > coin2[0] or coin2[0] >= n or 0 > coin2[1] or coin2[1] >= m) and (0<=coin1[0]<n and 0 <= coin1[1]<m):
        if minValue > ctn :
            minValue = ctn
        return
    elif (0 > coin1[0] or coin1[0] >= n or 0 > coin1[1] or coin1[1] >= m) and (0 > coin2[0] or coin2[0] >= n or 0 > coin2[1] or coin2[1] >= m):
        return
    if ctn == 10 :
        return

    for i in range(4):
        c1x,c1y = coin1[0]+nx[i],coin1[1]+ny[i]
        c2x,c2y = coin2[0]+nx[i],coin2[1]+ny[i]
        if 0<=c1x<n and 0<=c1y<m:
            if board[c1x][c1y] == "#":
                c1x,c1y = coin1[0],coin1[1]
        if 0<=c2x<n and 0<=c2y<m:
            if board[c2x][c2y] == "#":
                c2x,c2y = coin2[0],coin2[1]
        go([c1x,c1y],[c2x,c2y],ctn+1)
go(coins[0],coins[1],0)
if minValue >= 11 :
    minValue = -1
print(minValue)