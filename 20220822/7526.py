import collections
import time
def bfs(l,sx,sy,lx,ly):
    nx = [-2,-1,1,2,2,1,-1,-2]
    ny = [1,2,2,1,-1,-2,-2,-1]
    board = [[0] * l for _ in range(l)]
    d = collections.deque()
    d.append((sx,sy))
    check = True
    while d :
        sx,sy = d.popleft()
        for i in range(8):
            dx = sx+nx[i]
            dy = sy+ny[i]
            if 0<=dx<l and 0<=dy<l:
                board[dx][dy] = board[sx][sy] + 1
                if dx == lx and dy == ly :
                    return board[dx][dy]
                d.append((dx,dy))

n = int(input())
for _ in range(n):
    l = int(input())
    sx,sy = map(int,input().split())
    lx,ly = map(int,input().split())
    print(bfs(l,sx,sy,lx,ly))