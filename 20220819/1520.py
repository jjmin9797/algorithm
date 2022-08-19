n,m = map(int,input().split())

board = [[10001] * (m+1)]
for i in range(n):
    a = [10001]
    a += list(map(int,input().split()))
    board.append(a)
print(board)