import collections
n,m = map(int,input().split())

board = [[0 for _ in range(m)] for _ in range(n)]
blocks = list(map(int,input().split()))
result = 0
for i in range(m):
    for j in range(blocks[i]):
        board[j][i] = 1
for i in range(n):
    check = False
    sCount = 0
    for j in range(m):
        
        if board[i][j] == 0 and check :
            sCount += 1
        elif board[i][j] == 1 and not check :
            check = True
        elif board[i][j] == 1 and check :
            result += sCount
            sCount = 0
print(result)