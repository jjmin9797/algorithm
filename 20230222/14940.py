import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().strip().split())) for _ in range(n)]
answer = [[-1 for _ in range(m)] for _ in range(n)]
nxt = [(0, 1), (1, 0), (-1, 0), (0, -1)]
sx, sy = 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            sx, sy = i, j
            answer[sx][sy] = 0

        elif board[i][j] == 0:
            answer[i][j] = 0

queue = deque()
queue.append((sx, sy, 0))
while queue:
    x, y, cost = queue.popleft()
    for nx, ny in nxt:
        dx, dy = x + nx, y + ny
        if 0 <= dx < n and 0 <= dy < m and answer[dx][dy] == -1 and board[dx][dy] == 1:
            answer[dx][dy] = cost + 1
            queue.append((dx, dy, cost + 1))

for a in answer:
    print(" ".join(map(str, a)))
