n = int(input())
key = []
for i in range(n):
    a,b = map(int,input().split())
    key.append(a+b)

for i in range(n):
    print("Case #"+str(i+1)+":",key[i])
