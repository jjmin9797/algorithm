import sys
from collections import deque

input = sys.stdin.readline
strings = input().strip()
n = int(input())
commands = [input().strip().split() for _ in range(n)]
front_str = deque(list(strings))
back_str = deque()

for command in commands:
    if command[0] == "L" and front_str:
        back_str.appendleft(front_str.pop())
    elif command[0] == "D" and back_str:
        front_str.append(back_str.popleft())
    elif command[0] == "B" and front_str:
        front_str.pop()
    elif command[0] == "P":
        front_str.append(command[1])
print("".join(front_str + back_str))

# abcde    fg
