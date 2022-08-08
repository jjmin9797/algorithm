n = int(input())

result = [0,1,2,3]

for i in range(4,n+1):
    result.append(result[i-2]+result[i-1])
print(result[n]%10007)