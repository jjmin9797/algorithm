n = int(input())
dp = [0, 0]

for i in range(2, n + 1):
    nxt = []
    if i % 2 == 0:
        nxt.append(dp[i // 2])
    if i % 3 == 0:
        nxt.append(dp[i // 3])
    nxt.append(dp[i - 1])
    dp.append(min(nxt) + 1)
print(dp[n])
