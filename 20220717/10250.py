a = int(input())

for _ in range(a):
    #층,호,답
    h,w,n = map(int,input().split())
    result = []
    for i in range(1,w+1):
        for j in range(1,h+1):
            ho = str(i)
            if len(ho) == 1 :
                ho = "0"+str(i)
            
            result.append(str(j)+ho)
    print(result[n-1])