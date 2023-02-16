from collections import deque


def solution(order):
    order = deque(order)
    answer = 0
    box = deque()

    for i in range(1, len(order) + 1):
        box.append(i)
        while box and box[-1] == order[0]:
            answer += 1
            box.pop()
            order.popleft()
    return answer
