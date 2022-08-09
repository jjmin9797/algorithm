n = int(input())



board = list(map(int,input().split()))
d = [1]

for i in range(1,n):
    maxa = 1
    for j in range(i):
        if board[j] < board[i]:
            if maxa < d[j]+1 :
                maxa = d[j]+1
    d.append(maxa)
print(max(d))
