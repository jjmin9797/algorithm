a = int(input())
b = [int(input()) for _ in range(a)]
n = max(b)


result = [1,1,1]
rst = [[],[0,0,0,0],[0,1,0,0],[0,0,1,0]]

if n >= 3 :
    for i in range(3,n+1):
        e = 0
        t = [0]
        for j in range(1,4):
            
            t.append(result[i-j] - rst[j][j])
            e += result[i-j] - rst[j][j]
        
        rst.append(t)
        del rst[1]
        result.append(e)

for x in b :
    print(result[x])
print(rst)