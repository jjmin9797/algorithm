n,k = map(int,input().split())
coin = [int(input()) for _ in range(n)]

dp = [0]*(k+1)
#dp[0] = 1

for i in range(1,k+1):
    a = []
    for j in coin :
        if j <= i and dp[i-j] != -1 :
            a.append(dp[i-j])
    if not a :
        dp[i] = -1
    else :
        dp[i] = min(a) + 1
print(dp[-1])
            