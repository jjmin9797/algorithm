from collections import deque

n, d = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(n)]
answer = d
queue = deque()
queue.append([0, 0])

while queue:
    now, nowCost = queue.popleft()
    answer = min(answer, (d - now) + nowCost)
    for s, e, c in roads:
        if now <= s and e <= d:
            queue.append([e, nowCost + c + abs(s - now)])
print(answer)
