import collections
def check(a,b):
    n = len(a)
    ctn = 0
    for i in range(n):
        if a[i] == b[i] :
            ctn += 1
    if ctn  == n-1:
        return True
    else :
        return False




def solution(begin, target, words):
    
    if target not in words:
        return 0
    q = collections.deque()
    q.append((begin,0))
    visited = [-1 for _ in range(len(words))]
    while q:
        
        next,w = q.popleft()
        if next == target:
            return w
        for i in range(len(words)) :
            if visited[i] == -1 and  check(next,words[i]):
                q.append((words[i],w+1))
                visited[i] = w+1



    return 0
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))