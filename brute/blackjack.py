n,m = map(int,input().split())
numbers = list(map(int,input().split()))
result = 0
for x in range(n) :
    for y in range(x+1,n) :
        for z in range(y+1,n) :
            sumNumbers = numbers[x] + numbers[y] + numbers[z]
            if (sumNumbers <= m) and (result < sumNumbers) :
                result = sumNumbers
print(result)