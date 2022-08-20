import collections
import sys
dq = collections.deque()

n = int(input())
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        dq.append(int(command[1]))
    elif command[0] == 'pop':
        if len(dq) > 0 :
            print(dq.pop())
        else :
            print(-1)
    elif command[0] == 'size':
        print(len(dq))
    elif command[0] == 'empty' :
        if len(dq) > 0 :
            print(0)
        else :
            print(1)
    elif command[0] == 'top':
        if len(dq) > 0 :
            print(dq[-1])
        else :
            print(-1)