import collections

strs = input()
al = []
for i in range(97,123):
    al.append(chr(i))
key = collections.Counter(strs)

for a in al :
    if key[a] != None :
        print(key[a],end =" ")
    else :
        print(0,end =" ")