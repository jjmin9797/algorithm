import sys
n = int(input())
if n == 1 :
    b = int(input())
    print(b)
else :
    board = [int(sys.stdin.readline()) for _ in range(n)]
    d = [0] * (n+1)
    d[1] = board[0]
    d[2] = board[1] + board[0]
    board = [0]+board
    for i in range(3,n+1):
        d[i] = max(d[i-2]+board[i],d[i-3]+board[i-1]+board[i],d[i-1])
    print(d[-1])