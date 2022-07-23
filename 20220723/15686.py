import copy
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

house = 0
store = 0

for b in board :
    house += b.count(1)
    store += b.count(2)
ddd = store - m

def check(inBoard):
    bboard = copy.deepcopy(inBoard)
    size = len(bboard)
    storeList = []
    result = 0
    for i in range(size):
        for j in range(size):
            if 3 == bboard[i][j]:
                storeList.append([i,j])

    for i in range(size):
        for j in range(size):
            if 1 == bboard[i][j] :
                aaa = []
                for sl in storeList :
                    aaa.append((abs(i-sl[0])+abs(j-sl[1])))
                result += min(aaa)
            
    return result
checking = [True] * store
allChi = []
idxCheck = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 2 :
            idxCheck.append([i,j])


def go (idx,now) :
    
    if now == m :
        allChi.append(check(board))

        return
    for i in range(store):
        if checking[i] :
            checking[i] = False
            board[idxCheck[i][0]][idxCheck[i][1]] = 3
            go(0,now+1)
            checking[i] = True
            board[idxCheck[i][0]][idxCheck[i][1]] = 2
    

go(0,0)
print(min(allChi))
