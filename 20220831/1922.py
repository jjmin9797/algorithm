import collections
import sys


n = int(input())
m = int(input())
board = [[] for _ in range(n+1)]
check = [True for _ in range(n+1)]
check[0] = False
check[1] = False
for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    if a != b :
        board[a].append([b,c])
        board[b].append([a,c])
minVal = 10**10

def dfs(x,cost):

    global minVal
    if True not in check:
        minVal = min(minVal,cost)
        print(cost)
        return
    if cost >= minVal :
        return

    for i in board[x]:
        if check[i[0]] :
            check[i[0]] = False
            dfs(i[0],cost+i[1])
            check[i[0]] = True
dfs(1,0)
print(minVal)