#666 1666 2666 ... 9666
#11666 12666 13666 ... 99666

# 1 2 3 4 5 6 7 8 9
# 11 12 13 14 15 16 ... 99
# 111 112 ... 999
# 1111
movieNames = [666]

count = 1666
while len(movieNames) < 10000 :
    leng = str(count)
    if "666" in str(count) :
        movieNames.append(count)
    count += 1

n = int(input())
print(movieNames[n-1])


    