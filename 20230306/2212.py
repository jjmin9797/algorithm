import sys

input = sys.stdin.readline
n = int(input())
k = int(input())
board = list(map(int, input().strip().split()))
board.sort()


dist = []
if k >= n:
    print(0)
else:
    for i in range(1, n):
        dist.append(board[i] - board[i - 1])

    dist.sort(reverse=True)
    for i in range(k - 1):
        dist.pop(0)
    print(sum(dist))
