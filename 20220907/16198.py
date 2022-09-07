n = int(input())

b = list(map(int,input().split()))
maxValue = -1
def go(board,value) :
    global maxValue
    if len(board) == 2 :
        if maxValue < value :
            maxValue = value
        return
    
    for i in range(1,(len(board)-2)+1):
        go(board[:i]+board[i+1:],value+board[i-1]*board[i+1])


go(b,0)
print(maxValue)