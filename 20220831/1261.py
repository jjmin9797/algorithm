import collections

m,n = map(int,input().split())

board = [list(map(int,list(input()))) for _ in range(n)]
check = [[True]*m for _ in range(n)]
result = [[-1]*m for _ in range(n)]
check[0][0] = False
nx = [0,1,0,-1]
ny = [1,0,-1,0]
result[0][0] = 0
st = collections.deque()
st.append((0,0))
while st :
    x,y = st.popleft()
    for i in range(4):
        a = x+nx[i]
        b = y+ny[i]
        if 0 <= a < n and 0 <= b < m and result[a][b] == -1:
            if board[a][b] == 1 :
                result[a][b] = result[x][y] + 1
                st.append((a,b))
            elif board[a][b] == 0 :
                result[a][b] = result[x][y]
                st.appendleft((a,b))

print(result[n-1][m-1]) 

