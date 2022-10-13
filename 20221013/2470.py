import sys
n = int(input())
water = list(map(int,input().split()))
water.sort()

start = 0
end = n-1
minTake = sys.maxsize

while start < end :
    take = water[start] + water[end]
    if abs(take) < minTake :
        result = [water[start],water[end]]
        minTake = abs(take)
    
    if take > 0 :
        end -= 1
    elif take < 0 :
        start += 1
    else :
        break

print(result[0],result[1])