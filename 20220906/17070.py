n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]
garo = [[[0,1],[0,1]],[[0,1],[1,1]]]
sero = [[[1,0],[1,0]],[[1,0],[1,1]]]
dae = [[[1,1],[0,1]],[[1,1],[1,0]],[[1,1],[1,1]]]
garo = [(0,0),(0,2)]
sero = [(1,1),(1,2)]
dae = [(2,0),(2,1),(2,2)]
nx = [0,1,1]
ny = [1,0,1]

#가로 -> 0,1 0,1 / 0,1  1,1
#세로 -> 1,0 1,0 / 1,0  1,1
#대각 -> 1,1 0,1 / 1,1 1,0 / 1,1 1,1




ctn = 0
#[0,1],[0,2]
def dfs(left,right):
    global ctn
    if right[0] == n-1 and right[1] == n-1 :
        ctn += 1
        return

    #가로
    if left[0] == right[0] and left[1] != right[1] :
        for gx,gy in garo :
            aleft = [left[0] + nx[gx],left[1] + ny[gx]]
            bright = [right[0] + nx[gy],right[1] + ny[gy]]
            if 0 <= bright[0] < n and 0 <= bright[1] < n and board[bright[0]][bright[1]] != 1 :
                if gy == 2 : 
                    if board[bright[0]-1][bright[1]] != 1 and board[bright[0]][bright[1]-1] != 1:
                        dfs(aleft,bright)
                else :
                    dfs(aleft,bright)

        

    #세로
    elif left[0] != right[0] and left[1] == right[1] :
        for gx,gy in sero :
            aleft = [left[0] + nx[gx],left[1] + ny[gx]]
            bright = [right[0] + nx[gy],right[1] + ny[gy]]
            if 0 <= bright[0] < n and 0 <= bright[1] < n and board[bright[0]][bright[1]] != 1 :
                if gy == 2 : 
                    if board[bright[0]-1][bright[1]] != 1 and board[bright[0]][bright[1]-1] != 1:
                        dfs(aleft,bright)
                else :
                    dfs(aleft,bright)
        

    #대각
    else :
        for gx,gy in dae :
            aleft = [left[0] + nx[gx],left[1] + ny[gx]]
            bright = [right[0] + nx[gy],right[1] + ny[gy]]
            if 0 <= bright[0] < n and 0 <= bright[1] < n and board[bright[0]][bright[1]] != 1 :
                if gy == 2 : 
                    if board[bright[0]-1][bright[1]] != 1 and board[bright[0]][bright[1]-1] != 1:
                        dfs(aleft,bright)
                else :
                    dfs(aleft,bright)
dfs([0,0],[0,1])
print(ctn)