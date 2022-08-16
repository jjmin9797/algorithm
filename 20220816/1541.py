a = input()
b = a.split("-")
rst = []
for n in range(len(b)) :
    if "+" in b[n] :
        rst.append(sum(list(map(int,b[n].split("+")))))
    else :
        rst.append(int(b[n]))
count = rst[0]
for r in rst[1:] : 
    count -= r
print(count)