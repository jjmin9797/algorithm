board = [list(input()) for _ in range(5)]


maxLen = 0
for b in board:
    if maxLen < len(b) :
        maxLen = len(b)

for i in range(5):
    c = maxLen - len(board[i])
    for j in range(c):
        board[i].append('')

result = ''
for i in range(maxLen):
    for j in range(5):
        result += board[j][i]
print(result)