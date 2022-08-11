a,b,c = map(int,input().split())
value = a
rs = c-b



if rs <= 0:
    print(-1)
else :
    if rs == 1 :
        print(value // 1 + 1)
    elif value % rs == 0 :
        print(value // rs)
    

    else : 
        print(value // rs + 1)