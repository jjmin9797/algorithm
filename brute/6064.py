t = int(input())
for _ in range(t):
    m,n,x,y = map(int,input().split())
    #5 7 3 2
    x -= 1
    y -= 1
    #x = 2  y = 1
    k = x
    #x가 35을 넘지 않을 동안에 반복
    while k < n*m:
        # 2를 7로 나눈 나머지 = 2
        # 8 
        if k%n == y:
            print(k+1)
            break
        k += m
    else:
        print(-1)