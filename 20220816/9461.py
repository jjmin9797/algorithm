nums = [1,1,1,2,2]

for i in range(4,101):
    nums.append(nums[i]+nums[i-4])
n = int(input())
for i in range(n):
    a = int(input())
    print(nums[a-1])