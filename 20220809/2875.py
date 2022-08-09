n,m,k = map(int,input().split())

team = 0

while n >= 0 and m >= 0 :
    if n-2 >= 0 and m-1 >= 0 :
        n -= 2
        m -= 1
        team += 1   
    else :
        break

while n+m <= k :
    team -= 1
    n += 2
    m += 1
print(team)