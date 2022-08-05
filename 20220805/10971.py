n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

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

def valueCheck(x) :
    
    val = 0
    for i in range(len(x)-1) :
        b = board[x[i]][x[i+1]]
        if b == 0 :
            return -1
        else :
            val += b
    c = board[x[-1]][x[0]]
    if c == 0 :
        return -1
    else :
        val += c
    
    return val
nums = [i for i in range(n)]
minVal = valueCheck(nums)
while True :
    check,val = next_permutation(nums)
    value = valueCheck(val)
    
    if value < minVal and value != -1:
        minVal = value
    if not check :
        break
print(minVal)