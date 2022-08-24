import sys

v,e = map(int,sys.stdin.readline().split())
k = int(input())
board = [[] for _ in range(v+1)]
value = [10**10 for _ in range(v+1)]
check = [True for _ in range(v+1)]
for _ in range(e):
    a,b,c = map(int,sys.stdin.readline().split())
    board[a].append([b,c])
print(board)
check[k] = False
value[k] = 0
def dfs(idx,cost):
    
    for i in board[idx] :
        if check[i[0]] :
            check[i[0]] = False
            value[i[0]] = min(value[i[0]],cost+i[1])
            dfs(i[0],cost+i[1])
            check[i[0]] = True
dfs(k,0)

for g in range(1,len(value)):
    if value[g] == 10**10 :
        print("INF")
    else :
        print(value[g])