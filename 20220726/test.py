a = [1,2,3,4,4]
b = [1,1,2,3,4]


for i in range(3,-1,-1):
    a[i+1] = a[i]
print(a)