n = int(input())
nums = list(map(int,input().split()))
rs = []

for i in range(n):
    check=True
    for j in nums[i+1:]:
        if nums[i] < j:
            rs.append(j)
            check=False
            break
    if check :
        rs.append(-1)
print(rs)