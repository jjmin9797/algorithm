import sys
from collections import deque

input = sys.stdin.readline
# n = int(input())
# board = list(map(int, input().split()))
n = 8
board = [3, 7, 1, 6, 3, 5, 1, 7]
answer = []


def find(board, idx):
    print(idx, "=>")
    total = []
    now = board[idx]
    front = board[:idx]
    front.reverse()
    stack = deque()
    size = len(front)
    for i in range(size):
        if front[i] > now:
            if stack:
                if stack[-1][-1] < front[i]:
                    stack.append([size - i, front[i]])
            else:
                stack.append([size - i, front[i]])
    total += list(stack.copy())
    stack = deque()
    back = board[idx + 1 :]
    size = len(back)
    for i in range(size):
        if back[i] > now:
            if stack:
                if stack[-1][-1] < back[i]:
                    stack.append([idx + i + 2, back[i]])
            else:
                stack.append([idx + i + 2, back[i]])
    total += list(stack.copy())
    print(total)
    return [1, 1]


answer = []
for i in range(n):
    answer.append(find(board, i))
print(answer)
