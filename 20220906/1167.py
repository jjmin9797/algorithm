import sys
sys.setrecursionlimit(10 ** 9)


n = int(input())
graph = [[] for _ in range(n+1)]
check = [-1]*(n+1)

for _ in range(n):
    w = list(map(int,sys.stdin.readline().strip().split()))
    next = (len(w)-2)//2
    for i in range(1,next*2,2):
        graph[w[0]].append((w[i],w[i+1]))


def dfs(start,iw):
    for next,w in graph[start]:
        if check[next] == -1 :
            check[next] = iw+w
            dfs(next,w+iw)
check[1] = 0
dfs(1,0)
start = check.index(max(check))
check = [-1]*(n+1)
check[start] = 0
dfs(start,0)
print(max(check))
        