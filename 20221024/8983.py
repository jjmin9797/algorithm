import sys

m,n,l = map(int,input().split())
sadae = list(map(int,input().split()))
sadae.sort()
ani = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]

count = 0
for a,b in ani :
    start = 0
    end = len(sadae)-1

    while start < end :
        mid = (start+end) // 2
        if sadae[mid] < a:
            start = mid + 1
        else :
            end = mid
    
    if abs(sadae[end]-a)+b <= l or abs(sadae[end-1]-a)+b <= l :
        count += 1
print(count)
