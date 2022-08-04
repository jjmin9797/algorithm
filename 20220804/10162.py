#5분 1분 10초


t = int(input())

#300 60 10

if t % 10 == 0 :
    a = t//300
    t -= a*300
    b = t // 60
    t -= b*60
    c = t // 10
    print(a,b,c)
else :
    print(-1)