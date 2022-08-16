d = [[],[1,1,1,1,1,1,1,1,1,1]]

for i in range(2,1001):
    next = []
    for j in range(0,10):
        next.append(sum(d[i-1][j:10]))
    d.append(next)
n = int(input())
print(sum(d[n])%10007)
