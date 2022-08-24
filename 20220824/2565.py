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
dp = [1]
for i in range(1,n):
    maxa = 1
    for j in range(i):
        if line[j] < line[i] :
            if maxa < dp[j]+1 :
                maxa = dp[j]+1
    dp.append(maxa)
print(max(dp))
