dp = [0,1,2,2]

for i in range(4,1000001):
    dp.append((dp[i-1]+dp[i-2])%15746)
n = int(input())
print(dp[n])