import sys
from heapq import heappop, heappush

input = sys.stdin.readline
nxt = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def bfs(board, n):
    visited = [[float("inf") for _ in range(n)] for _ in range(n)]
    stack = []
    heappush(stack, [board[0][0], 0, 0])
    while stack:
        c, x, y = heappop(stack)
        for nx, ny in nxt:
            dx, dy = x + nx, y + ny
            if 0 <= dx < n and 0 <= dy < n:
                if visited[dx][dy] > c + board[dx][dy]:
                    visited[dx][dy] = c + board[dx][dy]
                    heappush(stack, [c + board[dx][dy], dx, dy])
    return visited[-1][-1]


ctn = 1
while True:
    n = int(input())
    if n == 0:
        break
    board = [list(map(int, input().strip().split())) for _ in range(n)]
    print(f"Problem {ctn}: {bfs(board,n)}")
    ctn += 1
