import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    sx, sy = map(int, input().split())
    stores = [list(map(int, input().strip().split())) for _ in range(n)]
    fx, fy = map(int, input().split())
    visited = [True for _ in range(n)]
    queue = deque()
    queue.append([sx, sy])
    answer = "sad"
    while queue:
        x, y = queue.popleft()
        if abs(x - fx) + abs(y - fy) <= 1000:
            answer = "happy"
            break

        for i in range(n):
            nx, ny = stores[i]
            if visited[i] and abs(x - nx) + abs(y - ny) <= 1000:
                visited[i] = False
                queue.append([nx, ny])

    print(answer)
