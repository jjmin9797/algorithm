import collections
n,m,t = map(int,input().split())
board = [list(map(int,input().split()))for _ in range(n)]
gong = []
nx = [0,1,0,-1]
ny = [1,0,-1,0]
for i in range(n):
    for j in range(m):
        if board[i][j] == -1:
            gong.append([i,j])
        
def hwak(board):
    b = [[0]*m for _ in range(n)]
    for i in gong:
        b[i[0]][i[1]] = -1
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                ctn = 0
                for k in range(4):
                    dx,dy = i+nx[k],j+ny[k]
                    if 0 <= dx < n and 0 <= dy < m and board[dx][dy] != -1 :
                        b[dx][dy] += int(board[i][j]/5)
                        ctn += int(board[i][j]/5)
                b[i][j] += board[i][j] - ctn
    return b

def gongi(board):
    b = [[-2]*m for _ in range(n)]

    x,y = gong[0]
    d = collections.deque()
    d.append(0)
    for i in range(1,m):
        b[x][i] = d.popleft()
        d.append(board[x][i])
    for i in range(x-1,-1,-1):
        b[i][m-1] = d.popleft()
        d.append(board[i][m-1])
    for i in range(m-2,-1,-1):
        b[0][i] = d.popleft()
        d.append(board[0][i])
    for i in range(1,x):
        b[i][0] = d.popleft()
        d.append(board[i][0])
    
    x,y = gong[1]
    d = collections.deque()
    d.append(0)
    for i in range(1,m):
        b[x][i] = d.popleft()
        d.append(board[x][i])
    for i in range(x+1,n):
        b[i][m-1] = d.popleft()
        d.append(board[i][m-1])
    for i in range(m-2,-1,-1):
        b[n-1][i] = d.popleft()
        d.append(board[n-1][i])
    for i in range(n-2,x-1,-1):
        b[i][0] = d.popleft()
        d.append(board[i][0])
    for i in gong:
        b[i[0]][i[1]] = -1
    for i in range(n):
        for j in range(m):
            if b[i][j] == -2 :
                b[i][j] = board[i][j]
    return b
    for bb in b :
        print(bb)


for _ in range(t):
    board = hwak(board)
    board = gongi(board)

result = 0
for b in board :
    result += sum(b)
print(result+2)

#n,1 n,m-1 + n-1,m-1 0,m-1 + 0,m-2 0,0 + 1,0 n-1,0