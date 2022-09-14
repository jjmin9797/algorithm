import collections

def bfs(start,visited,computers):
    st = collections.deque()
    visited[start] = 1
    st.append(start)
    while st :
        next = st.popleft()
        for i in range(len(computers)):
            if computers[next][i] == 1 and visited[i] == -1 :
                st.append(i)
                visited[i] = 1
    return visited



def solution(n, computers):
    answer = 0
    for i in range(n):
        for j in range(n):
            if i == j :
                computers[i][j] = 0

    visited = [-1 for _ in range(n)]
    ctn = 0
    for i in range(n):
        if visited[i] == -1 :
            visited = bfs(i,visited,computers)
            ctn += 1


    return ctn





print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))