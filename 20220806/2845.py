a,b = map(int,input().split())

nums = list(map(int,input().split()))

key = a*b
for n in  nums :
    print(n-key,end=" ")