import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs():
    while q:
        x, y = q.popleft()
        if visited[x][y] != "FIRE":
            flag = visited[x][y]
        else:
            flag = "FIRE"

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == -1 and (
                    board[nx][ny] == "." or board[nx][ny] == "@"
                ):
                    if flag == "FIRE":
                        visited[nx][ny] = flag
                    else:
                        visited[nx][ny] = flag + 1
                    q.append((nx, ny))
            else:
                if flag != "FIRE":
                    return flag + 1


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        m, n = map(int, input().split())
        q = deque()
        board = []
        visited = [[-1] * m for _ in range(n)]
        for i in range(n):
            board.append(list(input().strip()))
            for j in range(m):
                if board[i][j] == "@":
                    visited[i][j] = 0
                    start = (i, j)
                elif board[i][j] == "*":
                    visited[i][j] = "FIRE"
                    q.append((i, j))
        q.append(start)
        print(bfs())
