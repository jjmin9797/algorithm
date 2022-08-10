import sys
n = int(input())
board = [[]]
for _ in range(n):
    board.append(list(map(int,sys.stdin.readline().split())))
dp = [[],board[1]]

for i in range(2,n+1):
    a = board[i][0] + min(dp[i-1][1],dp[i-1][2])
    b = board[i][1] + min(dp[i-1][0],dp[i-1][2])
    c = board[i][2] + min(dp[i-1][0],dp[i-1][1])
    dp.append([a,b,c])

print(min(dp[n]))
