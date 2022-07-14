import sys
n,m = map(int,input().split())

a = [0]*m
def go(index, n, m,start):
    if index == m:
        sys.stdout.write(' '.join(map(str,a))+'\n')
        return
    for i in range(start, n+1):
        a[index] = i
        go(index+1, n, m,i)

go(0,n,m,1)