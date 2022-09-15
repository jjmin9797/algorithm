import sys

sys.setrecursionlimit(10 ** 9)
minNum = 10**10
def solution(n, start, end, roads, traps):
    answer = 0
    board = [[-1 for _ in range(n+1)] for _ in range(n+1)]

    for s,e,w in roads :
        board[s][e] = w
    global minNum
    
    def dfs(s,rs):
        global minNum
        if rs > minNum :
            return
        if s in traps :
            for x in range(n+1):
                board[s][x],board[x][s] = board[x][s],board[s][x]
        if s == end :
            minNum = min(rs,minNum)
            return

        for b in range(len(board[s])):
            if board[s][b] > 0 :
                dfs(b,board[s][b]+rs)


    dfs(start,0)     
    return minNum

print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2,3]))