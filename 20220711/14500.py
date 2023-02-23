n,m = map(int,input().split())
board = []
for i in range(n) :
    board.append(list(map(int,input().split())))
sumList = []
for i in range(n-1) :
    for j in range(m-1) :
        s = board[i][j] + board[i][j+1] + board[i+1][j] + board[i+1][j+1]
        sumList.append(s)


for i in range(n):
    for j in range(m-3) :
        r = board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3]
        sumList.append(r)

        
for i in range(n-3) :
    for j in range(m) :
        r = board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j]
        sumList.append(r)
#가로 6칸
for i in range(n-1) :
    for j in range(m-2) :
        # ㄱ자
        g = [board[i][j],board[i][j+1],board[i][j+2],
        board[i+1][j],board[i+1][j+1],board[i+1][j+2]]
        g1 = sum(g) - board[i][j] - board[i][j+1]
        g2 = sum(g) - board[i][j+1] - board[i][j+2]
        g3 = sum(g) - board[i+1][j] - board[i+1][j+1]
        g4 = sum(g) - board[i+1][j+1] - board[i+1][j+2]
        
        #번개
        t1 = board[i][j] + board[i][j+1] + board[i+1][j+1] + board[i+1][j+2]
        t2 = board[i+1][j] + board[i+1][j+1] + board[i][j+1] + board[i][j+2]

        #뻐큐
        f1 = board[i][j+1] + board[i+1][j] + board[i+1][j+1] + board[i+1][j+2]
        f2 = board[i][j] + board[i][j+1] + board[i][j+2] + board[i+1][j+1]

        sumList.extend([g1,g2,g3,g4,t1,t2,f1,f2])

for i in range(n-2) :
    for j in range(m-1) :
        #ㄱ자
        g = [board[i][j],board[i+1][j],board[i+2][j],
        board[i][j+1],board[i+1][j+1], board[i+2][j+1]]
        g1 = sum(g) - board[i][j] - board[i+1][j]
        g2 = sum(g) - board[i+1][j] - board[i+2][j]
        g3 = sum(g) - board[i][j+1] - board[i+1][j+1]
        g4 = sum(g) - board[i+1][j+1] - board[i+2][j+1]

        #번개
        t1 = board[i][j] + board[i+1][j] + board[i+1][j+1] + board[i+2][j+1]
        t2 = board[i][j+1] +board[i+1][j+1] + board[i+1][j] + board[i+2][j]

        #뻐큐
        f1 = board[i][j] + board[i+1][j] +board[i+2][j] + board[i+1][j+1]
        f2 = board[i][j+1] + board[i+1][j+1] + board[i+2][j+1] + board[i+1][j]
        sumList.extend([g1,g2,g3,g4,t1,t2,f1,f2])

print(max(sumList))
        