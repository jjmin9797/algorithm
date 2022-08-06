
# 2 3 4 5 6 7 8 9 10
# 2는 소수 (p)
# 3  5  7  9 
n , k = map(int,input().split())
nums = [i for i in range(2,n+1)]
result = []
while len(result) <= k and len(nums) != 0 :
    b = nums[0]
    result.append(b)
    del nums[0]
    
    for a in nums :
        if a % b == 0 :
            result.append(a)
            nums.remove(a)
    

print(result[k-1])