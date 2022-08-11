si,bun = map(int,input().split())

bun -= 45
if bun < 0 :
    si -= 1
    bun += 60
if si < 0 :
    si = 23
print(si,bun)