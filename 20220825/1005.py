import sys
import collections

t = int(input())
for _ in range(t):
    n,k = map(int,sys.stdin.readline().split())
    w = list(map(int,input().split()))
    w = [0]+w
    board = [[] for _ in range(n+1)]
    for i in range(k):
        a,b = map(int,sys.stdin.readline().split())
        board[b].append(a)
    end = int(input())
    bfsList = [[0] for _ in range(10000)]
    st = collections.deque()
    st.append((end,0))
    
    while st :
        nx,ctn = st.popleft()
        
        for i in board[nx] :
            if i not in bfsList[ctn+1]:
                bfsList[ctn+1].append(i)
            st.append((i,ctn+1))
    bfsList.reverse()
    bfsList[0] = 0
    for i in range(1,len(bfsList)):
        maxVal = 0
        for j in bfsList[i]:
            if maxVal < w[j] :
                maxVal = w[j]
        bfsList[i] = maxVal+bfsList[i-1]
    
    print(bfsList[-1]+w[end])

    