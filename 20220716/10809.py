a = input()
al = []
for i in range(97,123):
    al.append(chr(i))

result = []
for i in al :
    if i in a :
        result.append(a.index(i))
    else :
        result.append(-1)

print(' '.join(map(str,result)))