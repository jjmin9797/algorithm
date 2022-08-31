n = int(input())
m = int(input())
k = [0,1,2,3,4,5,6,7,8,9]
if m != 0 :
    key = list(map(int,input().split()))
    for ke in key :
        k.remove(ke)

else :
    print(len(str(n)))

