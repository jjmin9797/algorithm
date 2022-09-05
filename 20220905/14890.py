n,l = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    data = []
    for j in range(n):
        data.append(board[j][i])
    board.append(data)


ctn = 0
for b in board:
    check = [True]*(n)
    rs = True
    for i in range(1,n) :
        if b[i] == b[i-1] :
            continue
        #감소
        elif b[i] < b[i-1] and b[i-1]-b[i] == 1:
            
            if i+(l-1) < n :
                ck2 = True
                for j in range(1,l):
                    
                    if b[i] != b[i+j] or not check[i+j]:
                        
                        ck2 = False
                        break
                if ck2 :
                    for j in range(l):
                        check[i+j] = False
                    continue
                else :
                    rs = False
                    break
            else :
                rs = False
                break
        #증가
        elif b[i] > b[i-1] and b[i]-b[i-1] == 1:
            if 0 <= i-l :
                ck2 = True
                for j in range(1,l+1):
                    if b[i-1] != b[i-j] or not check[i-j]:
                        
                        ck2 = False
                        break
                if ck2 :
                    for j in range(1,l+1):
                        check[i-j] = False
                    continue
                else :
                    rs = False
            else :
                rs = False

        else :
            rs = False
            break
    if rs :
        #print(b)
        #print(check)
        ctn += 1
print(ctn)