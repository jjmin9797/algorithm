#1 
#2 3 4 5 6 7 
#8 9 10 11 12 13 14 15 16 17 18 19

#1 6 12 18 24 30 36
# 5  6  6

#6
#2 8 12
#8 19 18
#20 37 24
a = 6
start = 2
end = 8
n = 13
count = 2
while True :
    print(start,end)
    if start <= n < end :
        print(start,end,count)
        break
    else :
        a += 6
        start = end
        end += a
        count += 1
        
