import time
s = time.time()
result = ['1/1','1/2']
x = 2
y = 1
check = True
for i in range(2,10000001):
    result.append(str(x)+"/"+str(y))
    if x == 1 :
        y += 1
        check = False
        result.append(str(x)+"/"+str(y))
    if y == 1 :
        x += 1
        check = True
        result.append(str(x)+"/"+str(y))
    if check :
        x -= 1
        y += 1
    else :
        x += 1
        y -= 1
e = time.time()
print(e-s)
print(result[0:10])
print(len(result))


