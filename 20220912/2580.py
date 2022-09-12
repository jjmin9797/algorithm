board = [list(map(int,input().split())) for _ in range(9)]
board2 = [[] for _ in range(9)]
for b in board:
    for i in range(9):
        board2[i].append(b[i])
board3 = [[0,0,0,1,1,1,2,2,2],
        [0,0,0,1,1,1,2,2,2],
        [0,0,0,1,1,1,2,2,2],
        [3,3,3,4,4,4,5,5,5],
        [3,3,3,4,4,4,5,5,5],
        [3,3,3,4,4,4,5,5,5],
        [6,6,6,7,7,7,8,8,8],
        [6,6,6,7,7,7,8,8,8],
        [6,6,6,7,7,7,8,8,8]]
board4 = [[] for _ in range(9)]
for i in range(9):
    for j in range(9):
        board4[board3[i][j]].append(board[i][j])

for b in board4:
    print(b)






