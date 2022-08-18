import sys
d = [0,1,2,4]

for i in range(4,1000001):
    a = d[i-1]+d[i-2]+d[i-3]
    d.append(a%1000000009)
n = int(sys.stdin.readline())
for i in range(n):
    a = int(sys.stdin.readline())
    print(d[a])