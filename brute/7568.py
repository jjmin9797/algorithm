n = int(input())
students = [list(map(int,input().split())) for _ in range(n)]
rank = [1 for _ in range(n)]

for x in range(n) :
    for y in range(n) :
        if students[x][0] < students[y][0] and students[x][1] < students[y][1] :
            rank[x] += 1
for i in range(n):
    print(rank[i],end=" ")