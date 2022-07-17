aa = 4

result = [0] * (aa+1)

vvv = []
ctn = 0
def go(index, a):
    global ctn
    global vvv
    
    for i in range(1,a):
        result[index] = i
        if sum(result) == a :
            ctn += 1
            print(result)
            return
        elif sum(result) >= a :
            return
        print(result)
        go(index+1,a)

go(0,aa)
