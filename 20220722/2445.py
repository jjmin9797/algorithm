n = int(input())
k = (n*2) - 1
for i in range(1,n+1):
    print(("*"*i)+(" "*((2*n)-(2*i)))+("*"*i))
for i in range(n-1,0,-1):
    print(("*"*i)+(" "*((2*n)-(2*i)))+("*"*i))