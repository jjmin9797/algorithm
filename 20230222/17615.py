n = int(input())
board = list(input())


changeBoard = []
now = board[0]
ctn = 1
for b in board[1:]:
    if now == b:
        ctn += 1
    else:
        changeBoard.append(now + str(ctn))
        ctn = 1
        now = b
changeBoard.append(now + str(ctn))
redResult = 0
for cb in changeBoard:
    if cb[0] == "R":
        redResult += int(cb[1])

print(redResult)
