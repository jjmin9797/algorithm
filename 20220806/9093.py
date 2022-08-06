n = int(input())

for i in range(n):
    a = list(map(str,input().split()))
    for j in a :
        for x in range(len(j)-1,-1,-1):
            print(j[x],end="")
        print(" ",end="")
    print()