import sys
import collections

t = int(input())
for _ in range(t):
    n,k = map(int,sys.stdin.readline().split())
    d = list(map(int,input().split()))
    inDegree = [0 for _ in range(n+1)]
    graph = [[] for _ in range(n+1)]
    dp = [0 for _ in range(n+1)]
    st = collections.deque()
    for i in range(k):
        a,b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        inDegree[b] += 1
        
    w = int(input())

    for i in range(1,n+1):
        if inDegree[i] == 0 :
            st.append(i)
            dp[i] = d[i-1]
    
    while st :
        nx = st.popleft()
        for i in graph[nx]:
            inDegree[i] -= 1
            dp[i] = max(dp[i],dp[nx]+d[i-1])
            if inDegree[i] == 0 :
                st.append(i)
    print(dp[w])

    

    