import copy
n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
tree  = [[[] for _ in range(n)] for _ in range(n)]
mainBoard = [[5 for _ in range(n)] for _ in range(n)]
nextTree = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(-1,1),(1,-1),(1,1)]

for _ in range(m):
    x,y,old = map(int,input().split())
    tree[x-1][y-1].append(old)

liveTree = m

for _ in range(k):
    summer = []
    #봄
    for i in range(n):
        for j in range(n):
            tree[i][j].sort()
            for t in range(len(tree[i][j])):
                if tree[i][j][t] == 0 :
                    continue

                elif mainBoard[i][j] - tree[i][j][t] >= 0 :
                    mainBoard[i][j] -= tree[i][j][t]
                    tree[i][j][t] += 1
                else :
                    summer.append([i,j,tree[i][j][t]//2])
                    tree[i][j][t] = 0
                    liveTree -= 1
    
    for sx,sy,value in summer :
        mainBoard[sx][sy] += value

    
    #가을
    for i in range(n):
        for j in range(n):
            for t in range(len(tree[i][j])):
                if tree[i][j][t] != 0  and tree[i][j][t] % 5 == 0 :
                    for nx,ny in nextTree:
                        dx,dy = nx+i,ny+j
                        if 0<=dx<n and 0<=dy<n :
                            tree[dx][dy].append(1)
                            liveTree += 1
    
    for i in range(n):
        for j in range(n):
            mainBoard[i][j] += board[i][j]
            while 0 in tree[i][j]:
                tree[i][j].remove(0)
    
print(liveTree)
           
