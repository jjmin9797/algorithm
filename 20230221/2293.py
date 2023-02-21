from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [[0 for _ in range(k + 1)]]
dp[0][0] = 1

for i in range(len(coins)):
    ndp = dp[i].copy()
    ndp[0] = 1
    for j in range(coins[i], k + 1):
        ndp[j] += ndp[j - coins[i]]
print(dp[-1][-1])
