board = [list(input()) for _ in range(4)]
print(board)

def si(top):
    a = top[-1]
    for i in range(7,0,-1):
        top[i] = top[i-1]
    top[0] = a
    return top

def bansi(top):
    a = top[0]
    for i in range(7):
        top[i] = top[i+1]
    top[-1] = a
    return top
        

def turnCheck(f,s):
    if f[2] == s[6] :
        return False
    else :
        return True


n = int(input())
play = []
for _ in range(n):
    wa,we = map(int(input().split()))
    play.append([wa,we])

for i in play:
    wa = i[0]
    we = i[1]

    if wa == 1 :
        for j in range(3):
            if turnCheck(board[j],board[j+1]):
                if we == 1 :
                    board[j] = si(board[j])
                else :
                    board[j] = bansi(board[j])
                we *= -1
                continue
            else :
                if we == 1 :
                    board[j] = si(board[j])
                else :
                    board[j] = bansi(board[j])
                break
    elif wa == 2 :
        for j in range(1,3):
            if turnCheck(board[j],board[j+1]):
                if we == 1 :
                    board[j] = si(board[j])
                else :
                    board[j] = bansi(board[j])
                we *= -1
                continue
            else :
                if we == 1 :
                    board[j] = si(board[j])
                else :
                    board[j] = bansi(board[j])
                break
        if turnCheck(board[1],board[0]):
            pass
            





