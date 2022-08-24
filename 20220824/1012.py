import collections
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n,m,k = map(int,sys.stdin.readline().split())
    board = [[0]*m for _ in range(n)]
    
    for _ in range(k):
        x,y = map(int,sys.stdin.readline().split())
        board[x][y] = 1
    nx = [0,1,0,-1]
    ny = [1,0,-1,0]
    
    def bfs(dx,dy):
        
        st = collections.deque()
        st.append((dx,dy))
        if board[dx][dy] == 1 :
            board[dx][dy] = -1 
            while st :
                next = st.popleft()
                qx = next[0]
                qy = next[1]
                for z in range(4):
                    if 0 <= qx+nx[z] < n and 0<= qy+ny[z] < m and board[qx+nx[z]][qy+ny[z]] == 1 :
                        st.append((qx+nx[z],qy+ny[z]))
                        board[qx+nx[z]][qy+ny[z]] = -1
            return 1

        else :
            return 0
    ctn = 0
    for i in range(n):
        for j in range(m):
            ctn += bfs(i,j)
    print(ctn)


    