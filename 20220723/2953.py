
maxVal = 0
idx = 0
for i in range(1,6):
    a = list(map(int,input().split()))
    if maxVal < sum(a) :
        maxVal = sum(a)
        idx = i
print(idx,maxVal)