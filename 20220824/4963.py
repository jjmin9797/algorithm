import collections
import sys
while True :
    m,n = map(int,sys.stdin.readline().split())
    if m == 0 and n == 0 :
        break
    board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    nx = [1,0,-1,0,1,1,-1,-1]
    ny = [0,1,0,-1,1,-1,1,-1]
    def bfs(dx,dy):
        
        if board[dx][dy] == 1 :
            st = collections.deque()
            st.append((dx,dy))
            board[dx][dy] = -1
            while st :
                dx,dy = st.popleft()
                for i in range(8):
                    a = dx+nx[i]
                    b = dy+ny[i]
                    if 0 <= a < n and 0 <= b < m and board[a][b] == 1 :
                        board[a][b] = -1
                        st.append((a,b))
                        
            return 1

        else :
            return 0
    ctn = 0
    for i in range(n):
        for j in range(m):

            ctn += bfs(i,j)
    print(ctn)
