n,k = map(int,input().split())
coin = [int(input()) for _ in range(n)]

dp = [0]*(k+1)
#dp[0] = 1

for i in range(1,k+1):
    minValue = float("inf")
    for c in coin :
        if i-c >= 0 :
            if dp[i-c] < minValue :
                minValue = dp[i-c] + 1
    dp[i] = minValue
print(dp[-1])
            