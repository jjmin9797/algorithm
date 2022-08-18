count = 0
n = int(input())
for i in range(1,n+1):
    if len(str(i)) == 1 or len(str(i)) == 2 :
        count += 1
    else :
        check = []
        for j in range(0,2):
            a = int(str(i)[j]) - int(str(i)[j+1])
            check.append(a)
        if check[0] == check[1] :
            count += 1
        else : pass
print(count)

