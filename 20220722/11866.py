n,k = map(int,input().split())

numbers = [i for i in range(1,n+1)]
result = []
nextIdx = k-1
while len(numbers) >= 1 :


    result.append(numbers[nextIdx])
    del numbers[nextIdx]
    for i in range(k-1):
        if nextIdx >= len(numbers) :
            nextIdx = 0
        nextIdx += 1
    if nextIdx >= len(numbers) :
            nextIdx = 0    
    
print("<"+str(result)[1:-1]+">")

        