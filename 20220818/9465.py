n = int(input())

for i in range(n):
    t = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    board = [a,b]
    d = [[0,0],[0,0]]
    for j in range(2,t+2):
        x = max(d[j-2][1]+board[0][j-2],
        d[j-1][1]+board[0][j-2])
        y = max(d[j-2][0]+board[1][j-2],
        d[j-1][0]+board[1][j-2])
        d.append([x,y])
    print(max(d[-1]))
