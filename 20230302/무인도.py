from collections import deque

nxt = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def bfs(i, j, visited, maps, n, m):
    queue = deque()
    answer = int(maps[i][j])
    queue.append((i, j))
    visited[i][j] = False
    while queue:
        x, y = queue.popleft()
        for nx, ny in nxt:
            dx, dy = x + nx, y + ny
            if 0 <= dx < n and 0 <= dy < m and maps[dx][dy] != "X" and visited[dx][dy]:
                answer += int(maps[dx][dy])
                visited[dx][dy] = False
                queue.append((dx, dy))
    return answer


def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[True for _ in range(m)] for _ in range(n)]
    answer = []
    for i in range(n):
        for j in range(m):
            if maps[i][j] != "X" and visited[i][j]:
                answer.append(bfs(i, j, visited, maps, n, m))

    if answer:
        answer.sort()
        return answer
    return [-1]
