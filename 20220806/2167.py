n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]


k = int(input())

for i in range(k):
    result = 0
    i,j,x,y = map(int,input().split())
    for b in range(i-1,x):
        for c in range(j-1,y):
            print(b,c)
            result += board[b][c]
    print(result)