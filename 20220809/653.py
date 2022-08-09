n = int(input())

board = [[0]*2 for _ in range(91)]
board[0][1] = 1
board[1][0] = 1
for i in range(2,n+1):
    
    board[i][0] = board[i-1][0]+board[i-1][1]
    board[i][1] = board[i-1][0]
print(sum(board[n-1]))

