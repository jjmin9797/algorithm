import sys
import collections
import itertools
import copy
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
vs = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 2 :
            vs.append([i,j,0])
a = itertools.combinations(vs,m)
nx = [0,1,0,-1]
ny = [1,0,-1,0]
ctn = list(a)
print(ctn)
result = []
def check(boa):
    for i in boa:
        if 0 in i :
            return False
    return True
for i in range(len(ctn)):
    bo = copy.deepcopy(board)
    for tx,ty,tw in ctn[i]:
        bo[tx][ty] = 5
    st = collections.deque(ctn[i])
    mxnum = 0
    while st :
        if check(bo):
            break

        a,b,w = st.popleft()
        for j in range(4):
            dx = a+nx[j]
            dy = b+ny[j]
            if 0<=dx<n and 0<=dy<n and bo[dx][dy] == 0 :
                bo[dx][dy] = 1
                if w+1 > mxnum:
                    mxnum = w+1
                st.append([dx,dy,w+1])
            elif 0<=dx<n and 0<=dy<n and bo[dx][dy] == 2:
                bo[dx][dy] = 1
                if w+1 > mxnum:
                    mxnum = w+1
                st.append([dx,dy,w+1])
            


    if check(bo):
        result.append(mxnum)
    else :
        result.append(10**10)
    
if min(result) == 10**10 :
    print(-1)
else :
    print(min(result))
print(result)
    