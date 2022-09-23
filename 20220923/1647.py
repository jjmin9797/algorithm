import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x,y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y :
        parent[y] = x
    else :
        parent[x] = y

n,m = map(int,input().split())
parent = [0 for i in range(n+1)]
graph = []
for i in range(1,n+1):
    parent[i] = i

for i in range(m):
    a,b,c = map(int,input().split())
    graph.append([c,a,b])

graph.sort()
selected = []
answer = 0
for c,a,b in graph :
    if find_parent(a) != find_parent(b):
        union_parent(a,b)
        answer += c
        selected.append(c)
answer -= selected.pop()
print(answer)
print(parent)