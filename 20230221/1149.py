import sys

input = sys.stdin.readline

n = int(input())
houses = [list(map(int, input().split())) for _ in range(n)]

dp = [[], houses[0]]
for i in range(1, n):
    nxt = []
    for j in range(3):
        if j == 0:
            nxt.append(min(dp[i][1] + houses[i][j], dp[i][2] + houses[i][j]))
        elif j == 1:
            nxt.append(min(dp[i][0] + houses[i][j], dp[i][2] + houses[i][j]))
        elif j == 2:
            nxt.append(min(dp[i][0] + houses[i][j], dp[i][1] + houses[i][j]))
    dp.append(nxt)
print(min(dp[-1]))

# 14분 30초
