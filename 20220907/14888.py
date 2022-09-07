n = int(input())
nums = list(map(int,input().split()))
giho = list(map(int,input().split()))
minVal = 10**10
maxVal = -1
def go(idx,ctn,ccc):
    global minVal
    global maxVal
    if idx == (n-1) :
        if ctn > maxVal :
            maxVal = ctn
        if ctn < minVal :
            minVal = ctn
        return
    if giho[0] > 0 :
        giho[0] -= 1
        go(idx+1,ctn+nums[idx+1],ccc+"+")
        giho[0] += 1
    if giho[1] > 0 :
        giho[1] -= 1
        go(idx+1,ctn-nums[idx+1],ccc+"-")
        giho[1] += 1
    if giho[3] > 0 :
        giho[3] -= 1
        if ctn < 0:
            go(idx+1,(abs(ctn)//nums[idx+1])*-1,ccc+"/")
        else :
            go(idx+1,ctn//nums[idx+1],ccc+"/")
        giho[3] += 1
    if giho[2] > 0 :
        giho[2] -= 1
        go(idx+1,ctn*nums[idx+1],ccc+"*")
        giho[2] += 1

go(0,nums[0],"")
print(maxVal)
print(minVal)

