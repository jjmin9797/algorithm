b = ["a","e","i","o","u"]
while True :
    a = input()
    if a == "#" :
        break
    cou = 0
    for c in b :
        cou += a.count(c)
        cou += a.count(c.upper())
    print(cou)