a = list(input())


if len(a) % 2 == 1 :
    del a[len(a) // 2]
#0 -1      1 -2
check = True
for i in range(len(a)//2) :
    if a[i] == a[(i+1)*-1] :
        pass
    else :
        check = False
        break
if check :
    print(1)
else :
    print(0)