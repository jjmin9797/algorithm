n = int(input())

dp = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


for i in range(n - 1):
    now = dp.copy()
    for j in range(10):
        now[j] = sum(dp[j:]) % 10007
    dp = now.copy()
print(sum(dp) % 10007)


# 0 9
# 1 8
# 2 7
# 9 0 -> 55
