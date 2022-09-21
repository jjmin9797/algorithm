import sys
import collections

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]
cost = [0 for _ in range(n+1)]
result = [0 for _ in range(n+1)]
for i in range(1,n+1):
    next = list(map(int,input().split()))
    if len(next)  <= 2 :
        cost[i] = next[0]
        continue
    cost[i] = next[0]
    for j in range(1,len(next)-1):
        graph[next[j]].append(i)
        inDegree[i] += 1


q = collections.deque()
for i in range(1,n+1):
    if inDegree[i] == 0 :
        q.append((i,cost[i]))

while q :
    nxt,w = q.popleft()
    result[nxt] = w
    for g in graph[nxt]:
        inDegree[g] -= 1
        if inDegree[g] == 0 :
            q.append((g,w+cost[g]))

for r in range(1,len(result)):
    print(result[r])
