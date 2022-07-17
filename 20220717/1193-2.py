n = int(input())
x = []
x1 = 1
y = []
y1 = 2
while len(x) < 10000000 :
    for i in range(1,x1+1) :
        x.append(i)
    for i in range(x1-1,0,-1):
        x.append(i)
    for i in range(1,y1+1) :
        y.append(i)
    for i in range(y1-1,0,-1):
        y.append(i)
    x1 += 2
    y1 += 2
print(len(x))
print(str(x[n-1]) + "/" + str(y[n-1]))