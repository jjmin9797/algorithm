import sys
import collections

n,m = map(int,input().split())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
nx = [1,0]
ny = [0,1]
dp = [[-1 for _ in range(m)] for _ in range(n)]
dp[0][0] = board[0][0]
def bfs(x,y):
    st = collections.deque()
    st.append((x,y))
    while st :
        x,y = st.popleft()
        for i in range(2):
            a = x+nx[i]
            b = y+ny[i]
            if 0 <= a < n and 0 <= b < m :
                dp[a][b] = max(dp[a][b] , dp[x][y] + board[a][b])
                st.append((a,b))
bfs(0,0)
print(dp[n-1][m-1])
print(dp)