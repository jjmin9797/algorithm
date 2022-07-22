n = int(input())
ns = [int(input()) for _ in range(n)]

count = 0

def go (count,hap,n) :
    now = 0
    if hap > n :
        return 0
    if hap == n :
        return 1
    for i in range(1,4):
        now += go(count+1,hap+i,n)
    return now
for na in ns :
    print(go(0,0,na))
