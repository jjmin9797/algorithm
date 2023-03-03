from collections import deque


def bfs(visited, idx, cards):
    queue = deque()
    visited[idx] = False
    queue.append(idx)
    a = 1
    while queue:
        now = queue.popleft()
        nNode = cards[now - 1]
        if visited[nNode]:
            visited[nNode] = False
            a += 1
            queue.append(nNode)
    return a


def solution(cards):
    # [8,6,3,7,2,5,1,4]
    # [1,2,3,4,5,6,7,8]

    # [2,1]
    n = len(cards)

    visited = [True for _ in range(n + 1)]
    answer = []
    for i in range(n):
        if visited[i + 1]:
            answer.append(bfs(visited, i + 1, cards))
    if len(answer) > 1:
        answer.sort()
        return answer[-1] * answer[-2]
    return 0
