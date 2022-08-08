

nums = []
count = 1
while len(nums) < 1001 :
    for i in range(1,count+1):
        nums.append(count)
    count += 1
a,b = map(int,input().split())
print(sum(nums[a-1:b]))
#1 2 2 3 3 3 4 4 4 5 5 5 5 5 6 6 6 6 6 6 