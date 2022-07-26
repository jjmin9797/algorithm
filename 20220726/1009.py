n = int(input())
testCase = [list(map(int,input().split())) for _ in range(n)]

for x in testCase:
    startNum = x[0]
    nextNum = startNum
    count = 0
    banbock = [startNum]
    while True :

        

        nextNum = startNum * nextNum
        banbock.append(int(str(nextNum)[-1]))
        count += 1
        if str(nextNum)[-1] == str(startNum):
            break
    del banbock[-1]
    
    if x[1] % len(banbock) == 0 :
        print(banbock[-1])
    else :
        print(banbock[x[1]%len(banbock) - 1])
    