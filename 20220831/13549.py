import collections
n,k = map(int,input().split())
board = [-1 for _ in range(200000)]

dk = collections.deque()
dk.append((n,0))
board[n] = 0
while dk :
    x,c = dk.popleft()
    if x-1 >= 0 and board[x-1] == -1:
        dk.append((x-1,board[x]+1))
        board[x-1] = c+1
    if x+1 < 200000 and board[x+1] == -1:
        dk.append((x+1,board[x]+1))
        board[x+1] = c+1

    if x*2 < 200000 and board[x*2] == -1:
        dk.appendleft((2*x,board[x]))
        board[2*x] = c
print(board[0:100])
