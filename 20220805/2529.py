n = int(input())

board = input().split()
nums = [True] * 10
ans = []
last = []

def go(key):
    global last
    global nums
    global ans
    global n
    if len(key) == n+1 :
        
        checkPoint = True
        for i in range(len(key)-1):
            if board[i] == "<":
                if key[i] < key[i+1] :
                    pass
                else :
                    checkPoint = False
                    break
            elif board[i] == ">":
                if key[i] > key[i+1] :
                    pass
                else :
                    checkPoint = False
                    break
            
        if checkPoint :
            if len(ans) == 0 :
                ans = key
            if len(ans) == 1 and len(last) == 0 :
                last = key
            
            return 
        else :
            return 

        
    
    for i in range(0,10):
        if nums[i] :
            nums[i] = False
            go(key+[i])
            if len(ans) == 3 :
                nums = [True] * 10
                key = []
                for i in range(9,-1,-1):
                    if nums[i] :
                        nums[i] = False
                        go(key+[i])
                        if len(last) == 3 :
                            return
                        nums[i] = True


                return
                
            nums[i] = True

    
go([])
print(ans,last)
#print(ans)