n = int(input())
board = []
dp = []
for _ in range(n):
    board.append(list(map(int,input().split())))
dp.append(board[-1])
board.reverse()
for i in range(n-1):    
    bb = []
    for j in range(len(board[i])-1):
        bb.append(board[i+1][j] + max(dp[i][j], dp[i][j+1]))
    dp.append(bb)
print(dp[-1][0])
    

