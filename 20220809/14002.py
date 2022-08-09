n = int(input())
a = list(map(int,input().split()))
d = [0]*n
v = [-1]*n
for i in range(n):
    d[i]
    for j in range(i):
        if a[j] < a[i] and d[j]+1 > d[i]:
            d[i] = d[j]+1
            v[i] = j
ans = max(d)
print(enumerate(d))
p = [i for i,x in enumerate(d) if x == ans][0]
print(p)
print(d)
print(v)