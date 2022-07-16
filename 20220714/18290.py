n,m,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
maxNumbers = [0] * k
indexNumber = [(-1,-1)] * k


print(maxNumbers,indexNumber)

for i in range(n):
    for j in range(m):
        if board[i][j] > min(maxNumbers) :
            indexNumber[maxNumbers.index(min(maxNumbers))] = (i,j)
            maxNumbers[maxNumbers.index(min(maxNumbers))] = board[i][j]
            
print(maxNumbers)
print(indexNumber)