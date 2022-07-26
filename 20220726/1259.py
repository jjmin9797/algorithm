while True :
    a = input()
    if a == '0' :
        break
    else :
        a = list(map(int,a))
    
    length = len(a)
    if length % 2 == 1 :
        del a[length//2]
    a.insert(0,'X')
    check = True
    for i in range(1,length//2+1):
        if a[i] == a[-i] :
            pass
        else :
            check = False
            break
    if check :
        print("yes")
    else :
        print("no")