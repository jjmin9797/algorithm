import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [list(map(int, list(input().strip()))) for _ in range(n)]


visited = [[True for _ in range(n)] for _ in range(n)]
nx = [0, 1, 0, -1]
ny = [1, 0, -1, 0]


def bfs(x, y, board, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = False
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx, dy = x + nx[i], y + ny[i]
            if 0 <= dx < n and 0 <= dy < n and board[dx][dy] == 1 and visited[dx][dy]:
                visited[dx][dy] = False
                queue.append((dx, dy))
                count += 1
    return count


answer = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and visited[i][j]:
            answer.append(bfs(i, j, board, visited))
answer.sort()
print(len(answer))
for a in answer:
    print(a)
