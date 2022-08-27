import collections
n,k = map(int,input().split())

st = collections.deque()
for i in range(1,n+1):
    st.append(i)
#1,2,3,4,5,6,7
#3,4,5,6,7,1,2
result = []
while len(st) > 0 :
    for i in range(k-1):
        a = st.popleft()
        st.append(a)
    result.append(st.popleft())
print(result)
