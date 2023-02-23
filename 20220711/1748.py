n = int(input())
length = len(str(n))
result = 0
for i in range(1,length) :
    result += i * (9 * ((10 ** i)//10))
result += (n - ((10 ** length)//10) + 1 ) * length
print(result )


