import collections
import sys
n = int(input())

for _ in range(n):
    dp = [-1 for _ in range(10000)]
    
    start,end = map(str,input().split())
    if len(start) != 4 :
        start = (4-len(start))*"0"+start
    st = collections.deque()
    st.append((start,""))
    dp[int(start)] = ""
    while st :
        
        nx , command = st.popleft()
        if int(nx) == int(end) :
            break
        if len(nx) != 4 :
            nx = (4-len(nx))*"0"+nx
        if int(nx) * 2 > 9999 :
            n1 = (int(nx*2))%10000
        else :
            n1 = int(nx)*2
        if dp[n1] == -1 :
            dp[n1] = command+"D"
            st.append((str(n1),command+"D"))
        
        n2 = int(nx)-1
        if n2 == 0 :
            n2 = 9999
        if dp[n2] == -1 :
            dp[n2] = command+"S"
            st.append((str(n2),command+"S"))
        
        n3 = collections.deque(list(nx))
        n3.append(n3.popleft())
        n3 = "".join(n3)
        if dp[int(n3)] == -1 :
            st.append((n3,command+"L"))
            dp[int(n3)] = command+"L"
        

        n4 = collections.deque(list(nx))
        n4.appendleft(n4.pop())
        n4 = "".join(n4)
        if dp[int(n4)] == -1 :
            st.append((n4,command+"R"))
            dp[int(n4)] = command+"R"
    print(dp[int(end)])
        

        
            
