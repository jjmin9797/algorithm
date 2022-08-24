import collections
import sys

n = int(input())
m = int(input())
board = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    board[a].append(b)
    board[b].append(a)
check = [[True] for _ in range(n+1)]
check[1] = False
def bfs(idx):
    ctn = 0
    st = collections.deque()
    st.append(idx)
    while st :
        next = st.popleft()
        for x in board[next]:
            if check[x] :
                check[x] = False
                ctn += 1
                st.append(x)

    return ctn
print(bfs(1))


