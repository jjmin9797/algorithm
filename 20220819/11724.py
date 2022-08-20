import sys

sys.setrecursionlimit(100000)
n,m = map(int,input().split())
board = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    board[a].append(b)
    board[b].append(a)
check = [True] * (n+1)
count = 0
def dfs(start) :
    for i in board[start]:
        if check[i] :
            check[i] = False
            dfs(i)
for i in range(1,n+1):
    if check[i] :
        dfs(i)
        count += 1
print(count)