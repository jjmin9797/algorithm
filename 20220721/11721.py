a = input()
count = 0
strs = ""
for s in a :
    strs += s
    count += 1
    if count == 10 :
        print(strs)
        count = 0
        strs = ""
if len(strs) > 0 :
    print(strs)