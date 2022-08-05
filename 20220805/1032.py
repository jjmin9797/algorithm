n = int(input())
strs = [list(input()) for _ in range(n)]

length = len(strs[0])
key = ""
for i in range(length):
    check = strs[0][i]
    a = True
    for s in strs:
        if s[i] == check :
            pass
        else :
            key += "?"
            a = False 
            break
    if a :
        key += check
print(key)
