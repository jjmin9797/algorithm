n = int(input())
board = list(map(int,input().split()))
dp = [0] * n

for i in range(n):
    dp[i] = board[i]
    for j in range(i):
        if board[i] > board[j] and dp[j]+board[i] > dp[i] :
            dp[i] = dp[j] + board[i]
print(max(dp))