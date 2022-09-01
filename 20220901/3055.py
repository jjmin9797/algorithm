import collections
import sys

input = sys.stdin.readline

n,m = map(int,input().strip().split())

board = [list(input().strip()) for _ in range(n)]
check = [[True]*m for _ in range(n)]
sWater = []
for i in range(n):
    for j in range(m):
        if board[i][j] == "D":
            end = [i,j]
        elif board[i][j] == "*":
            check[i][j] = False
            sWater.append([i,j,0])
        elif board[i][j] == "S":
            start = [i,j]
        elif board[i][j] == "X":
            check[i][j] == False



nx = [0,1,0,-1]
ny = [1,0,-1,0]

wSt = collections.deque()
st = collections.deque()

start.append(0)
if len(sWater) > 0 :
    for ww in sWater:
        wSt.append(ww)
st.append(start)

while st :
    def wGo():

        wx,wy,t = wSt.popleft()
        check[wx][wy] = False
        for i in range(4):
            a = wx+nx[i]
            b = wy+ny[i]
            if 0 <= a < n and 0 <= b < m and board[a][b] != "X" and board[a][b] != "D" and board[a][b] != "*":
                board[a][b] = "*"
                check[a][b] = False
                wSt.append([a,b,t+1])
    def sGo():

        gx,gy,t = st.popleft()
        check[gx][gy] = False
        for i in range(4):
            a = gx+nx[i]
            b = gy+ny[i]
            if 0 <= a < n and 0 <= b < m and board[a][b] != "*" and board[a][b] != "X" and check[a][b]:                
                check[a][b] = False
                st.append([a,b,t+1])
            
                
    if len(wSt) > 1:

        if wSt[0][2] == st[0][2] :
            wGo()
        
        elif wSt[0][2] > st[0][2] :
            sGo()
        elif wSt[0][2] < st[0][2] :
            wGo()
    else :
        sGo()

    if len(st) == 0 :
        print("KAKTUS")
        break
    if board[st[0][0]][st[0][1]] == "D":
        print(st[0][2])
        break
    

    
