from collections import deque
k = int(input())
m,n = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]
dp = [[[0 for _ in range(31)] for _ in range(m)] for _ in range(n)]
nextHorse = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
nextMonkey = [(0,1),(1,0),(-1,0),(0,-1)]

q = deque()
q.append([0,0,k])
result = -1
while q :
    x,y,nk = q.popleft()
    if x == n-1 and y == m-1 :
        result = dp[x][y][nk]
        break
    for nx,ny in nextMonkey:
        dx,dy = x+nx,y+ny
        if 0<=dx<n and 0<=dy<m and board[dx][dy] != 1 and dp[dx][dy][nk] == 0 :
            dp[dx][dy][nk] = dp[x][y][nk] + 1
            q.append([dx,dy,nk])

    if nk > 0 :
        for nx,ny in nextHorse:
            dx,dy = x+nx,y+ny
            if 0 <= dx < n and 0 <= dy < m and board[dx][dy] != 1 and dp[dx][dy][nk-1] == 0:
                 dp[dx][dy][nk-1] = dp[x][y][nk]+1
                 q.append([dx,dy,nk-1])
print(result)