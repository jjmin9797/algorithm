import collections
import sys
queue = collections.deque()
n,m = map(int,input().split())
board = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    board[a].append(b)
    inDegree[b] += 1

for i in range(1,n+1):
    if inDegree[i] == 0 :
        queue.append(i)
result = []
while queue:
    tmp = queue.popleft()
    result.append(tmp)
    for i in board[tmp]:
        inDegree[i] -= 1
        if inDegree[i] == 0 :
            queue.append(i)
print(" ".join(list(map(str,result))))
