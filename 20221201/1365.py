import sys

def lower_bount(s,e,v):
    while s < e :
        m = (s + e) // 2
        if res[m] < v :
            s = m + 1
        else :
            e = m
    return e

res = []
n = int(sys.stdin.readline())
line = list(map(int,sys.stdin.readline().strip().split()))

for i in range(n):
    if i == 0 :
        res.append(line[0])
    if res[-1] < line[i]:
        res.append(line[i])
    else :
        tmp = lower_bount(0,len(res),line[i])
        res[tmp] = line[i]


print(n-len(res))