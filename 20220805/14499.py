#이동한 칸의 수가 0 -> 주사위바닥 -> 칸
#0이 아닌 수 -> 칸에있는 수 -> 바닥 칸(0)

n,m,x,y,k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

command = map(int,input().split())
print(board)