import sys
n = int(input())
water = list(map(int,input().split()))
water.sort()
sumValue = sys.maxsize
result = []

for i in range(n-2):
    start = i+1
    end = n-1
    while start < end :
        take = water[start]+water[end]+water[i]
        if abs(take) < sumValue :
            sumValue = abs(take)
            result = [water[i],water[start],water[end]]
        if take < 0 :
            start += 1
        elif take > 0 :
            end -= 1
        else :
            break
print(*result)