import collections
def solution(n, m, x, y, r, c, k):
    answer = ''
    board = [[0 for _ in range(m)] for _ in range(n)]
    start = [x,y]
    end = [r-1,c-1]
    nx = [1,0,0,-1]
    ny = [0,-1,1,0]
    msg = ["d","l","r","u"]
    q = collections.deque()
    q.append([x-1,y-1,""])
    rs = []
    ctn = 0
    while q :
        ctn += 1
        ox,oy,road = q.popleft()
        if [ox,oy] == end :
            rs.append(road)
            
        
        for i in range(4):
            dx,dy = ox+nx[i],oy+ny[i]
            
            if 0<=dx<n and 0<=dy<m and board[dx][dy] == 0:
                board[dx][dy] = -1
                q.append([dx,dy,road+msg[i]])
        

    road = rs[0]
    check = k-len(road)
    if (k-len(road)) % 2 != 0:
        return "impossible"
    elif check == 0 :
        return road
    else :
        return ("du"*(check//2))+road
        if "u" in road and ("r" in road or "u" in road) and x+1 <= n:
            return ("du"*(check//2))+road
        elif "u" in road and ("r" in road or "u" in road) and x+1 > n :
            for i in range(len(road)-1):
                if road[i] != road[i+1]:
                    return road[:i+1]+("ud"*(check//2))+road[i+1:]
        elif "d" in road and "r" in road and y-1 >= 1:
            for i in range(len(road)-1):
                if road[i] != road[i+1]:
                    return road[:i+1]+("lr"*(check//2))+road[i+1:]
        elif "d" in road and "r" in road and y-1 < 1:
            for i in range(len(road)-1):
                if road[i] != road[i+1]:
                    return road[:i+2]+("lr"*(check//2))+road[i+2:]
        elif "d" in road and "l" in road:
            return road + ("rl"*(check//2))
        
        

                    
    return answer

print(solution(3,4,1,1,3,4,11))