board = [i**2 for i in range(2,317)]

n = int(input())
d = [0] * (n+1)
d[0] = 0
d[1] = 1
d[2] = 2

next = 1
for i in range(3,n+1):
    if i in board :
        next = i
        d[i] = 1
        continue
    if i % 2 == 0:
        mina = 100000
        for j in range(i//2):  
            if mina > d[i-1-j] + d[0+i] :
                mina = d[i-1-j] + d[0+i]
        if mina > (d[i//2]*2) :
            mina = (d[i//2]*2)
        d[i] = mina
        pass
    else :
        mina = 100000
        for j in range(i//2):  
            if mina > d[i-1-j] + d[0+i] :
                mina = d[i-1-j] + d[0+i]
        d[i] = mina
            #

    #i-1 and 0+1
    #i-2 and 0+2
print(d[n])
