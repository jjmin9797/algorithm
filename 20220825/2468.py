import sys
import collections
import copy
n = int(input())
nx = [0,1,0,-1]
ny = [1,0,-1,0]
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
result = [1]
for i in range(1,102):
    b = copy.deepcopy(board)
    st = collections.deque()
    ctn = 0
    for x in range(n):
        for y in range(n):
            if b[x][y] > i :
                st.append((x,y))
                while st :
                    x,y = st.popleft()
                    for u in range(4):
                        dx = x+nx[u]
                        dy = y+ny[u]
                        if 0<=dx<n and 0<=dy<n and b[dx][dy] > i and b[dx][dy] != -1:
                            st.append((dx,dy))
                            b[dx][dy] = -1
                ctn += 1
    result.append(ctn)
print(max(result))


