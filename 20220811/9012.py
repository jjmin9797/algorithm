n = int(input())
r = []
for bb in range(n):
    a = input()
    result = []
    check = True
    for b in a :
        if b == "(" :
            result.append(b)
        elif b == ")":
            if len(result) == 0 :
                check = False
                break   
            else :
                result.pop()
    if len(result) == 0 and check :
        r.append("Yes")
    else :
        r.append("No")
for i in range(n):
    print(r[i])