import sys
import copy
n = int(input())
minBoard = [0,0,0]
maxBoard = [0,0,0]
for i in range(n):
    a,b,c = map(int,sys.stdin.readline().split())
    xa = maxBoard[0]+a
    xb = maxBoard[1]+b
    xc = maxBoard[2]+c
    na = minBoard[0]+a
    nb = minBoard[1]+b
    nc = minBoard[2]+c
    maxBoard[0] += max(xa,xb)
    maxBoard[1] += max(xa,xb,xc)
    maxBoard[2] += max(xb,xc)
    minBoard[0] += min(na,nb)
    minBoard[1] += min(na,nb,nc)
    minBoard[2] += min(nb,nc)

print(max(maxBoard),min(minBoard))
