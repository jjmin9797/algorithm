board = [list(input()) for _ in range(4)]
print(board)

def si(top):
    a = top[-1]
    for i in range(7,0,-1):
        top[i] = top[i-1]
    top[0] = a
    return top

def bansi(top):
    a = top[0]
    for i in range(7):
        top[i] = top[i+1]
    top[-1] = a
    return top
        

print(si([1,0,1,0,1,1,1,1]))
#n = int(input())

