import collections
n,m = map(int,input().split())

board = [list(map(int,list(input()))) for _ in range(n)]
check = [[[0,0]for _ in range(m)] for _ in range(n)]
check[0][0][0] = 1

nx = [1,0,-1,0]
ny = [0,1,0,-1]
def bfs(x,y,wall):
    st = collections.deque()
    st.append((x,y,wall))
    while st :
        x,y,wall = st.popleft()
        if x == n-1 and y == m-1 :
            return check[x][y][wall]

        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if dx < 0 or dy < 0 or dx >= n or dy >= m :
                continue
            if board[dx][dy] == 1 and wall == 0 :
                check[dx][dy][wall+1] = check[x][y][wall]+1
                st.append((dx,dy,wall+1))
            if board[dx][dy] == 0 and check[dx][dy][wall] == 0 :
                st.append((dx,dy,wall))
                check[dx][dy][wall] = check[x][y][wall]+1
    return -1
print(bfs(0,0,0))
