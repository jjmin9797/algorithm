import sys

input = sys.stdin.readline
from collections import deque

t = int(input())
for _ in range(t):
    beer = 20
    n = int(input())
    sx, sy = map(int, input().strip().split())
    store = [list(map(int, input().strip().split())) for _ in range(n)]
    fx, fy = map(int, input().strip().split())
    queue = deque()
    queue.append([sx, sy])
    visited = [0 for i in range(n + 1)]
    answer = "sad"
    while queue:
        x, y = queue.popleft()
        if abs(x - fx) + abs(y - fy) <= 1000:
            answer = "happy"
            break
        for i in range(n):
            if not visited[i]:
                new_x, new_y = store[i]
                if abs(x - new_x) + abs(y - new_y) <= 1000:
                    queue.append([new_x, new_y])
                    visited[i] = 1
    print(answer)
