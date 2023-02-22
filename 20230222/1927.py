from heapq import heappop, heappush

n = int(input())
commands = [int(input()) for _ in range(n)]
heap = []

for command in commands:
    if command == 0:
        if heap:
            print(heappop(heap))
        else:
            print(0)
    elif command != 0:
        heappush(heap, command)
