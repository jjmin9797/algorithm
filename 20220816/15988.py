d = [0,1,2,4]

for i in range(4,1000000):
    a = d[i-1]+d[i-2]+d[i-3]
    d.append(a%1000000009)
n = int(input())
for i in range(n):
    a = int(input())
    print(d[a])