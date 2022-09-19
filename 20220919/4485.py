import collections
import sys
next = [(0,1),(1,0),(0,-1),(-1,0)]
while True :
    n = int(input())
    if n == 0 :
        break
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    board = [list(map(int,input().split())) for _ in range(n)]
    dp[0][0] = board[0][0]
    q = collections.deque()
    q.append((0,0))
    while q :
        x,y = q.popleft()
        for i in next:
            nx,ny = x+i[0],y+i[1]
            if 0<=nx<n and 0<=ny<n and dp[nx][ny] == -1 :
                if nx == 0 :
                    dp[nx][ny] = dp[nx][ny-1] + board[nx][ny]
                elif ny == 0 :
                    dp[nx][ny] = dp[nx-1][ny] + board[nx][ny]
                else :
                    dp[nx][ny] = min(dp[nx][ny-1],dp[nx-1][ny]) + board[nx][ny]
                q.append((nx,ny))
    for d in dp:
        print(d)

    
    
