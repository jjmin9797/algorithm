def solution(seat):
    result = -1
    length = len(seat)
    #[1,1],[1,-1],[-1,1],[-1,-1]
    nextx = [[1,0],[2,0],[-1,0],[-2,0]]
    nexty = [[0,1],[0,2],[0,-1],[0,-2]]
    for i in range(length):
        for j in range(length):
            if seat[i][j] == "O":
                ctn = 1
                for dx,dy in nextx:
                    nx,ny = i+dx,j+dy
                    if 0<=nx<length and 0<=ny<length and seat[nx][ny] == "O":
                        ctn += 1
                if result < ctn :
                    result = ctn
                ctn = 1
                for dx,dy in nexty:
                    nx,ny = i+dx,j+dy
                    if 0<=nx<length and 0<=ny<length and seat[nx][ny] == "O":
                        ctn += 1
                if result < ctn :
                    result = ctn
    return result





    
    

print(solution([['O','O','X'],['O','O','O'],['O','X','O']]))