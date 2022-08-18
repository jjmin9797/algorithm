d = [[],[1,1,1]]

for i in range(2,100001):
    a = d[i-1][0]+d[i-1][2]
    b = d[i-1][1]+d[i-1][2]
    c = d[i-1][0] + d[i-1][1] + d[i-1][2]
    
    d.append([a%9901,b%9901,c%9901])
n = int(input())
print((sum(d[n])%9901))