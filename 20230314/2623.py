import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
inDgree = [0 for _ in range(n + 1)]
board = [[] for _ in range(n + 1)]
queue = deque()
for _ in range(m):
    order = list(map(int, input().strip().split()))
    for i in range(order[0] - 1):
        board[order[i + 1]].append(order[i + 2])
        inDgree[order[i + 2]] += 1


for i in range(1, n + 1):
    if inDgree[i] == 0:
        queue.append(i)


answer = []
while queue:
    nxt = queue.popleft()
    answer.append(nxt)
    for i in board[nxt]:
        inDgree[i] -= 1
        if inDgree[i] == 0:
            queue.append(i)

if len(answer) == n:
    for a in answer:
        print(a)
else:
    print(0)
