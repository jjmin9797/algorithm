a = list(input())
b = list(input())
len1 = len(a)
len2 = len(b)
board = [[0] * (len2+1) for _ in range(len1+1)]

for i in range(1,len1+1):
    for j in range(1,len2+1):
        if a[i-1] == b[j-1] :
            board[i][j] = board[i-1][j-1]+1
        else :
            board[i][j] = max(board[i-1][j],board[i][j-1])
print(board[-1][-1])