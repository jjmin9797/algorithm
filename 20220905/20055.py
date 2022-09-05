import collections
n,k = map(int,input().split())
belt = list(map(int,input().split()))
up = collections.deque(belt[0:n])
down = collections.deque(belt[n:2*n])
down.reverse()
lobot = collections.deque([0]*n)
ctn = 0
rs = 0
while ctn < k :
    down.append(up.pop())
    up.appendleft(down.popleft())
    lobot.pop()
    lobot.appendleft(0)
    if lobot[-1] == 1 :
        lobot[-1] = 0

    lb = [0]*n
    for i in range(len(lobot)) :
        if lobot[i] == 1  :
            if up[i+1] > 0 and lobot[i+1] != 1:
                lb[i+1] = 1
                up[i+1] -= 1
            else :
                lb[i] = 1
    lobot = collections.deque(lb)
        
    

    if lobot[-1] == 1 :
        lobot[-1] = 0
    if up[0] > 0 :
        up[0] -= 1
        lobot[0] = 1
    ctn = up.count(0) + down.count(0)
    if ctn > k :
        break
    rs += 1
print(rs)
