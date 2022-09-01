import collections
import sys
input = sys.stdin.readline

n,l,r = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
check = [[True]*n for _ in range(n)]
nx =[0,1,0,-1]
ny =[1,0,-1,0]


def bfs(x,y):
    st = collections.deque()
    st.append((x,y))
    sum = board[x][y]
    nextIdx = [[x,y]]
    check[x][y] = False
    while st :
        x,y = st.popleft()
        for i in range(4):
            a = x+nx[i]
            b = y+ny[i]
            if 0 <= a < n and 0 <= b < n and l <= abs(board[x][y] - board[a][b]) <= r and check[a][b]:
                check[a][b] = False
                st.append((a,b))
                nextIdx.append([a,b])
                sum += board[a][b]
    val = int(sum/len(nextIdx))

    for i in nextIdx:
        board[i[0]][i[1]] = val
    if len(nextIdx) > 1 :
        return 1
    else : 
        check[x][y] = True
        return 0
        

stop = -1
ctn = 0
while True:
    stop = 0
    check = [[True]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if check[i][j] :
                stop += bfs(i,j)

    if stop == 0 :
        break
    else : ctn += 1

print(ctn)