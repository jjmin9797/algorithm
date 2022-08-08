a = int(input())
b = [int(input()) for _ in range(a)]
n = max(b)


result = [1,1,2]

if n >= 3 :
    for i in range(3,n+1):
        a = result[i-2]+result[i-1]+result[i-3]
        result.append(a)
for x in b :
    print(result[x])