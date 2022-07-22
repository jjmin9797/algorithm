
l,c = map(int,input().split())
board = list(map(str,input().split()))
board.sort()
checkB = [True]*c
rst = ['']*l
aaa = []
mmo = ['a','e','i','o','u']
jja = ['b', 'c' ,'d', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
def go(idx,l,c) :
    if idx >= l :
        maxVal = 0
        sortCheck = True
        for i in range(l):
            if ord(rst[i]) > maxVal :
                maxVal = ord(rst[i])
                pass
            else :
                sortCheck = False
                return
        if sortCheck :
            ja = 0 # 2개 이상
            mo = 0 # 1개 이상
            for i in rst:
                if i in mmo :
                    mo += 1
                elif i in jja :
                    ja += 1
                
            if ja >= 2 and mo >= 1 :
                print(''.join(rst))
                pass

        return
    
    for i in range(c):
        if checkB[i] :
            rst[idx] = board[i]
            checkB[i] = False
            go(idx+1,l,c)
            checkB[i] = True
            rst[idx] = ''
go(0,l,c)
