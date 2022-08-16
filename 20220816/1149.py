n = int(input())
board = []
d = []

for i in range(n):
    board.append(list(map(int,input().split())))
d.append(board[0])
for i in range(1,n):
    t1 = board[i][0] + min(d[i-1][1],d[i-1][2])
    t2 = board[i][1] + min(d[i-1][0],d[i-1][2])
    t3 = board[i][2] + min(d[i-1][1],d[i-1][0])
    d.append([t1,t2,t3])
print(min(d[-1]))
