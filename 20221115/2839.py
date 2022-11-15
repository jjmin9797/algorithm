sugar = int(input())
dp = [0,-1,-1,1,-1,1,2]

if sugar >= 6 :
    for i in range(7,5001):
        bag3 = dp[i-3]
        bag5 = dp[i-5]
        if bag3 == -1 and bag5 == -1 :
            dp.append(-1)
        elif bag3 != -1 and bag5 == -1 :
            dp.append(bag3+1)
        elif bag3 == -1 and bag5 != -1 :
            dp.append(bag5+1)
        elif bag3 != -1 and bag5 != -1 :
            dp.append(min(bag3,bag5)+1)
    print(dp[sugar])
else :
    print(dp[sugar])
print(dp[0:100])