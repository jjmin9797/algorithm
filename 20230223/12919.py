from collections import deque

start = input()
end = input()
startSize = len(start)
queue = deque([end])
answer = False
while queue:
    nxt = queue.popleft()

    if nxt == start:
        answer = True
        break
    if len(nxt) > startSize:
        if nxt[-1] == "A":
            queue.append(nxt[:-1])
        if nxt[0] == "B":
            nxt = nxt[::-1]
            queue.append(nxt[:-1])

if answer:
    print(1)
else:
    print(0)
