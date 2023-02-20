from heapq import heappop, heappush

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
nxt = [(0, 1), (1, 0), (-1, 0), (0, -1)]
queue = []
for i in range(n):
    for j in range(n):
        # if board[i][j] == 0:
        #     board[i][j] = float("inf")
        if board[i][j] != 0:
            heappush(queue, (0, i, j, board[i][j]))
            board[i][j] = [board[i][j], -1]
            continue
        board[i][j] = [board[i][j], 0]


while queue:
    time, nowX, nowY, name = heappop(queue)
    if s <= time:
        break
    for nx, ny in nxt:
        dx, dy = nowX + nx, nowY + ny
        if 0 <= dx < n and 0 <= dy < n:
            if board[dx][dy][1] == 0:
                board[dx][dy][1] = time
                board[dx][dy][0] = name
                heappush(queue, (time + 1, dx, dy, name))
            elif board[dx][dy][1] == time:
                if board[dx][dy][0] < name:
                    continue
                board[dx][dy][0] = name
                board[dx][dy][1] = time
                heappush(queue, (time + 1, dx, dy, name))

# for b in board:
#     print(b)
print(board[x - 1][y - 1][0])
