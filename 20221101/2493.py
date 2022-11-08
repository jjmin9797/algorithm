import collections
n = int(input())
board = list(map(int,input().split()))
result = [0 for _ in range(n)]
stack = []


for i in range(len(board)):
    while stack:
        if board[stack[-1][0]] < board[i] :
            stack.pop()
        else :
            result[i] = stack[-1][0] + 1
            break
    stack.append((i,board[i]))
print(*result)
