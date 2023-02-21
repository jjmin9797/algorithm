import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[board[0][0]]]

for i in range(1, n):
    nxt = []
    for j in range(i + 1):
        if j == 0:
            nxt.append(board[i][0] + dp[i - 1][0])

        elif j == i:
            nxt.append(board[i][-1] + dp[i - 1][-1])

        else:
            nxt.append(max(dp[i - 1][j - 1], dp[i - 1][j]) + board[i][j])
    dp.append(nxt)
print(max(dp[-1]))

# 10분 20초
