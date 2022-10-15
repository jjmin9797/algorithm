import sys
n = int(input())
water = list(map(int,input().split()))
water.sort()

start = 0
end = n-1
minTake = sys.maxsize
result = []
while start < end :
    take = water[start]+water[end]
    if abs(take) < minTake :
        minTake = abs(take)
        result = [water[start],water[end]]
    
    if take > 0 :
        end -= 1
    elif take < 0 :
        start += 1
    else :
        break
print(result[0],result[1])