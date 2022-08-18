n = int(input())
d = [0]*n
board = list(map(int,input().split()))
d[0] = board[0]
for i in range(1,n):
    d[i] = board[i]
    if d[i] < d[i-1]+board[i] :
        d[i] = d[i-1]+board[i]
print(d)