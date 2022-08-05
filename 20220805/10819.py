n = int(input())

nums = list(map(int,input().split()))

nums.sort()

def next_permutation(a):
    i = len(a)-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return False,a
    j = len(a)-1
    while a[j] <= a[i-1]:
        j -= 1

    a[i-1],a[j] = a[j],a[i-1]

    j = len(a)-1
    while i < j:
        a[i],a[j] = a[j],a[i]
        i += 1
        j -= 1

    return True,a

def valueCheck(v):
    i = len(v)
    result = 0
    for j in range(i-1):
        result += abs(v[j] - v[j+1])
    return result

maxVal = -1
while True :
    check,val = next_permutation(nums)
    value = valueCheck(val)
    
    if value > maxVal :
        maxVal = value
    if not check :
        break
print(maxVal)