import sys
from collections import deque

input = sys.stdin.readline


def rotationCheck(rotationBoard, idx, direction):
    rotationBoard[idx] = direction
    left, right = idx - 1, idx + 1
    if 0 <= left < t and rotationBoard[left] == 0 and gears[idx][6] != gears[left][2]:
        rotationBoard[left] = direction * -1
        rotationCheck(rotationBoard, left, direction * -1)

    if (
        0 <= right < t
        and rotationBoard[right] == 0
        and gears[idx][2] != gears[right][6]
    ):
        rotationBoard[right] = direction * -1
        rotationCheck(rotationBoard, right, direction * -1)


def rotationGear(gears, rotationBoard):
    for i in range(t):
        if rotationBoard[i] == 1:
            q = deque(gears[i])
            q.appendleft(q.pop())
            gears[i] = list(q)

        elif rotationBoard[i] == -1:
            q = deque(gears[i])
            q.append(q.popleft())
            gears[i] = list(q)


def countS(gears):
    answer = 0
    for g in gears:
        if g[0] == 1:
            answer += 1
    return answer


t = int(input())
gears = [list(map(int, list(input().strip()))) for _ in range(t)]
k = int(input())
commands = [list(map(int, input().strip().split())) for _ in range(k)]
for idx, direction in commands:
    rotationBoard = [0 for _ in range(t)]
    idx -= 1
    rotationCheck(rotationBoard, idx, direction)
    rotationGear(gears, rotationBoard)
print(countS(gears))
