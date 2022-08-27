import sys
n = int(input())
board = []
for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    board.append((a,b))
board.sort()
line = []
for b in board:
    line.append(b[1])
print(line)
dp = [1] * n
for i in range(1,n):

    for j in range(i):
        if line[j] < line[i] :
        
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))

