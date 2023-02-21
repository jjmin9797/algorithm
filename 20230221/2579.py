import sys

input = sys.stdin.readline

n = int(input())
board = [int(input()) for _ in range(n)]
if n == 1:
    print(board[0])
else:
    board = [0] + board
    dp = [0, board[1], board[1] + board[2]]
    for i in range(3, n + 1):
        dp.append(max(dp[i - 3] + board[i - 1] + board[i], dp[i - 2] + board[i]))
    print(dp[n])
