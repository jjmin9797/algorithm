n = int(input())
result = [0,0,1,1,2,3,2]
if n >= 7 :
    for i in range(7,n+1) :
        nextCheck = [float('inf'),float('inf'),float('inf')]
        if i % 2 == 0 :
            nextCheck[0] = result[i // 2]
        if i % 3 == 0 :
            nextCheck[1] = result[i // 3]
        nextCheck[2] = result[i-1]
        result.append(min(nextCheck)+1)
print(result[n])

