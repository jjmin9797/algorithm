import sys
import collections
n,m,start = map(int,input().split())
board = [[] for _ in range(n+1)]
check = [True] * (n+1)
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    board[a].append(b)
    board[b].append(a)
result = []
def dfs(s):
    result.append(s)
    check[s] = False
    board[s].sort()
    for b in board[s]:
        if check[b] :
            dfs(b)
dfs(start)
result = map(str,result)
print(" ".join(result))

result2 = []
check = [True] * (n+1)
st = collections.deque()
st.append(start)
result2.append(start)
check[start] = False
while len(st) != 0 :
    board[st[0]].sort()
    for b in board[st[0]] :
        if check[b] :
            check[b] = False
            st.append(b)
            result2.append(b)
            
    st.popleft()
result2 = map(str,result2)
print(" ".join(result2))
    
        

