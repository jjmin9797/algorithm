nums = []

for i in range(1,101):
    nums.append(i**2)
result = []
n = int(input())
m = int(input())
for num in nums :
    if n <= num <= m :
        result.append(num)
if len(result) > 0 :

    print(sum(result))
    print(min(result))
else :
    print(-1)