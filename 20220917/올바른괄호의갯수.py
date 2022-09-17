def solution(n):
    
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(2,n):
        for j in range(0,i+1):
            dp[i+1] += dp[i-j]*dp[j]
    

    
    return dp[n]
solution(1)