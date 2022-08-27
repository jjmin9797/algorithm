import collections
n = int(input())
st = collections.deque()

for i in range(1,n+1):
    st.append(i)

while len(st) > 1 :
    st.popleft()
    a = st.popleft()
    st.append(a)

print(st.pop())