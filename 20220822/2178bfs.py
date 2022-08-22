import sys
import collections
sys.setrecursionlimit(1000000)
n,m = map(int,input().split())
board = [list(map(int,list(input()))) for _ in range(n)]
#check = [[True] * m for _ in range(n)]

nx = [0,1,0,-1]
ny = [1,0,-1,0]
#check[0][0] = False

def bfs(x,y):
    st = collections.deque()
    st.append((x,y))
    while st:
        x,y = st.popleft()
        for i in range(4):
            dx = x+nx[i]
            dy = y+ny[i]
            if 0 <= dx < n and 0<= dy < m and board[dx][dy] == 1 :
                st.append((dx,dy))
                board[dx][dy] = board[x][y] + 1
    return board[n-1][m-1]
print(bfs(0,0))
for b in board:
    print(b)

