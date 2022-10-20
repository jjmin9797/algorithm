import sys
n,m = map(int,input().split())
checkPoint = []
for _ in range(n):
    checkPoint.append(int(sys.stdin.readline().strip()))
checkPoint.sort()

start = 0
end = min(checkPoint) * m
result = 0
while start <= end :
    time = 0
    mid = (start+end)//2
    for t in checkPoint :
        time += mid // t
    
    if time >= m :
        result = mid
        end = mid - 1
    else :
        start = mid + 1
print(result)