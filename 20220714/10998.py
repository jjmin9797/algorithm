n = input()
start = n
ctn = 0
while True :
    if len(n) == 1 :
        n = "0" + n
    n = n[-1] + str(int(n[0])+int(n[1]))[-1]
    ctn += 1
    if n[0] == "0":
        n = n[-1]
    if start == n :
        print(ctn)
        break

