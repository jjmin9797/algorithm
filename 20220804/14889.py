n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

player = [True] * (n)
choo = []


def check(team,nn):
    count1 = 0
    count2 = 0
    rTeam = []
    for i in range(nn):
        if i not in team :
            rTeam.append(i)
    for x in team :
        for y in team :
            count1 += board[x][y]
    
    for x in rTeam :
        for y in rTeam :
            count2 += board[x][y]
    
    return abs(count1-count2)

minVal = 99999999
def go(idx,na) :
    global minVal
    global choo
    if idx == na//2 :
        if minVal > check(choo,na):
            minVal = check(choo,na)
        return

    for i in range(na):
        if player[i] :
            player[i] = False
            choo.append(i)
            go(idx+1,na)
            player[i] = True
            del choo[-1]
go(0,n)
print(minVal)    