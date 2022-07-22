import copy
import time
n = int(input())
#numbers = [int(input()) for _ in range(n)]
start = time.time()
numbers = [i for i in range(500000)]
key1 = sum(numbers) / len(numbers)
key1 = format(key1,".0f")

if int(key1) == -0 :
    print(0)
else :
    print(key1)

numbers.sort()
print(numbers[n//2])

numbers2 = copy.deepcopy(numbers)
numbers2 = set(numbers2)
numbers2 = list(numbers2)
maxVal = 0
resultList = []
for num in numbers2 :
    a = numbers.count(num)
    if maxVal == a :
        resultList.append(num)
    if maxVal < a :
        resultList = []
        resultList.append(num)
        maxVal = a

if len(resultList) == 1 :
    print(resultList[0])
else :
    resultList.sort()
    print(resultList[1])
print(max(numbers)-min(numbers))
        
end = time.time()
print(end-start)