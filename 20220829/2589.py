import collections
n,m = map(int,input().split())
board = [list(input()) for _ in range(n)]
check = [[True]*m for _ in range(n)]
nx = [0,1,-1,0]
ny = [1,0,0,-1]

def bfs(x,y):

    check[x][y] = False
    st = collections.deque()
    st.append((x,y,0))
    rs = -1
    while st :
        x,y,c = st.popleft()
        rs = max(c,rs)
        for i in range(4):
            dx = x+nx[i]
            dy = y+ny[i]
            if 0 <= dx < n and 0 <= dy < m and board[dx][dy] == "L" and check[dx][dy] :
                st.append((dx,dy,c+1))
                check[dx][dy] = False
    return rs
rs = -1
for i in range(n):
    for j in range(m):
        if board[i][j] == "L":
            check = [[True]*m for _ in range(n)]
            rs = max(bfs(i,j),rs)
print(rs)