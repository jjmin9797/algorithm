#245
result = []
for i in range(1,1000055):
    length = len(str(i))
    strings = str(i)
    sum = 0
    for j in range(length) :
        sum += int(strings[j])
    result.append([i,i+sum])

keyList = []
n = int(input())

for i in range(len(result)):
    if result[i][1] == n :
        keyList.append(result[i][0])

if len(keyList) >= 1 :
    print(min(keyList))
else :
    print(0)

