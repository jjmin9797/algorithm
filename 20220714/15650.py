import sys
n,m = map(int,input().split())
c = [False]*(n+1)
a = [0]*m
def go(index, n, m, start):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(start, n+1):
        if c[i]:
            continue
        
        c[i] = True
        a[index] = i
        go(index+1, n, m,i+1)
        c[i] = False
go(0,n,m,1)