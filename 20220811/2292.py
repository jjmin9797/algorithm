#1 
#2 3 4 5 6 7 
#8 9 10 11 12 13 14 15 16 17 18 19

#1 6 12 18 24 30 36
# 5  6  6

#6
#2 8 12
#8 19 18
#20 37 24
n = int(input())
if n == 1 :
    print(1)
else :
    a = 6
    start = 2
    end = 8

    count = 2
    while True :

        if start <= n < end :
            print(count)
            break
        else :
            a += 6
            start = end
            end += a
            count += 1
        
