import collections
import sys
n = int(input())
board = [list(input()) for _ in range(n)]
board2 = []
for b in board:
    t = []
    for a in range(n):
        if b[a] == "G" :
            t.append("R")
        else :
            t.append(b[a])
    board2.append(t)

nx = [0,1,0,-1]
ny = [1,0,-1,0]
def bfs2(x,y):
    if board2[x][y] != -1 :
        nextColor = board2[x][y]
        board2[x][y] = -1
        st = collections.deque()
        st.append((x,y))
        while st :
            (x,y) = st.popleft()
            for i in range(4):
                a = x+nx[i]
                b = y+ny[i]
                if 0 <= a < n and 0 <= b < n and board2[a][b] == nextColor :
                    st.append((a,b))
                    board2[a][b] = -1
        return 1
    else :
        return 0

def bfs(x,y):
    if board[x][y] != -1 :
        nextColor = board[x][y]
        board[x][y] = -1
        st = collections.deque()
        st.append((x,y))
        while st :
            (x,y) = st.popleft()
            for i in range(4):
                a = x+nx[i]
                b = y+ny[i]
                if 0 <= a < n and 0 <= b < n and board[a][b] == nextColor :
                    st.append((a,b))
                    board[a][b] = -1
        return 1
    else :
        return 0
ctn1 = 0
ctn2 = 0
for i in range(n):
    for j in range(n):
        ctn1 += bfs(i,j)
        ctn2 += bfs2(i,j)
print(ctn1,ctn2)