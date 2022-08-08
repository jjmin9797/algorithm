board = [[0 for _ in range(100)] for _ in range(100)]

n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    for a in range(x,x+10):
        for b in range(y,y+10):
            if board[a][b] == 0 :
                board[a][b] = 1
result = 0
for i in board :
    result += i.count(1)
print(result)