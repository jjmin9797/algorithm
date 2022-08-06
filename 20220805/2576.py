nums = []
for _ in range(7):
    nums.append(int(input()))
results = []
for n in nums :
    if n % 2 == 1 :
        results.append(n)
if len(results) > 0 :
    print(sum(results))
    print(min(results))
else :
    print(-1)