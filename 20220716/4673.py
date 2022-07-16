result = []
for i in range(1,10001):
    count = i
    for j in str(i):
        count += int(j)
    result.append(count)
result.sort()
for i in range(1,101):
    if i in result :
        pass
    else :
        print(i)
