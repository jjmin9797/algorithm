


saram = 0
maxSaram = 0
for i in range(4):
    
    nae , tan = map(int,input().split())
    saram -= nae
    if maxSaram < saram :
        maxSaram = saram
    saram += tan
    if maxSaram < saram :
        maxSaram = saram
print(maxSaram)