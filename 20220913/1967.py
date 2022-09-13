import sys
import collections
n = int(input())
m = int(input())
graph = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(n)]
city = list(map(int,input().split()))
rs = []
visited = [0 for _ in range(n)]
visited[city[0]-1] = 1
rs.append(city[0]-1)
st = collections.deque()
st.append(city[0]-1)
while st :
    next = st.popleft()
    for x in range(n):
        if graph[next][x] == 1 and visited[x] == 0:
            visited[x] = 1
            st.append(x)
            rs.append(x)
print(rs)