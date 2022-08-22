import collections

n,k = map(int,input().split())
d = collections.deque()
board = [-1] * 100002
board[n] = 0
d.append(n)

while d :
    a = d.popleft()
    na = [a+1,a-1,a*2]
    for i in range(3):
        if 0 <= na[i] <= 100001 and board[na[i]] == -1 :
            board[na[i]] = board[a]+1
            d.append(na[i])
print(board[k-1])