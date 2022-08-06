a = [5,2,3,1,4]
a.sort()

def nextSoon(x):
    i = len(x)-1
    while i > 0 and x[i-1] > x[i]:
        i -= 1
    if i <= 0 :
        return False
    